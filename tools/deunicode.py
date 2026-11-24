r"""Keep the Typst sources ASCII-only, except for accented Latin letters.

    python3 tools/deunicode.py file.typ ...           list the other non-ASCII characters
    python3 tools/deunicode.py --check file.typ ...   same, exit status 1 if there are any
    python3 tools/deunicode.py --apply file.typ ...   replace them in place

Each character is replaced according to its context:
  markup  shorthands (--- -- ...) or #sym.<name>, else a \u{...} escape
  math    symbol names (approx, ->, <=, times...), else a \u{...} escape
  string  \u{...} escape
  raw, comments  an ASCII approximation
Check the result with `make check-ascii` and by comparing the PDFs.
"""
import re, sys, collections, unicodedata

KEYWORDS = {'let', 'set', 'show', 'import', 'include', 'if', 'for', 'while', 'return', 'context', 'break', 'continue'}

def allowed(c):
    """Accented Latin letters (é, ü, Å...) are kept."""
    return ord(c) < 128 or (unicodedata.category(c).startswith('L') and 'LATIN' in unicodedata.name(c, ''))


def scan(t):
    """Yield (index, context) for every non-ASCII character."""
    out = []
    st = [('markup', None)]
    i, n = 0, len(t)
    def top(): return st[-1][0]
    while i < n:
        c = t[i]
        k = top()
        if k == 'hash':                      # postfix chain after #ident
            if c == '(':
                st.append(('code', ')')); i += 1; continue
            if c == '[':
                st.append(('content', None)); i += 1; continue
            if c == '.' and i + 1 < n and (t[i+1].isalpha() or t[i+1] == '_'):
                i += 1
                while i < n and (t[i].isalnum() or t[i] in '_-'): i += 1
                continue
            st.pop(); continue                # end of expression: reprocess c
        if ord(c) > 127:
            out.append((i, 'markup' if k in ('markup', 'content') else ('math' if k == 'math' else 'code')))
            i += 1; continue
        # comments (all contexts except strings/raw)
        if t.startswith('//', i) and not (k in ('markup', 'content') and re.search(r'https?:$', t[max(0, i-6):i])):
            j = t.find('\n', i); j = n if j < 0 else j
            out += [(p, 'comment') for p in range(i, j) if ord(t[p]) > 127]
            i = j; continue
        if t.startswith('/*', i):
            j = t.find('*/', i); j = n if j < 0 else j + 2
            out += [(p, 'comment') for p in range(i, j) if ord(t[p]) > 127]
            i = j; continue
        if k in ('markup', 'content'):
            if c == '\\':
                i += 2; continue
            if c == '`':
                m = re.match(r'`+', t[i:]); b = len(m.group())
                if b == 2: i += 2; continue
                j = t.find('`' * b, i + b); j = n if j < 0 else j + b
                out += [(p, 'raw') for p in range(i, j) if ord(t[p]) > 127]
                i = j; continue
            if c == '$':
                st.append(('math', None)); i += 1; continue
            if c == '#':
                i += 1
                if i < n and t[i] in '({[':
                    st.append(('hash', None))
                    continue
                m = re.match(r'[A-Za-z_][\w-]*', t[i:])
                if m:
                    word = m.group(); i += len(word)
                    if word in KEYWORDS: st.append(('code', '\n'))
                    else: st.append(('hash', None))
                continue
            if c == '[':
                st.append(('content', None)); i += 1; continue
            if c == ']' and k == 'content':
                st.pop(); i += 1; continue
            i += 1; continue
        if k == 'math':
            if c == '\\': i += 2; continue
            if c == '$': st.pop(); i += 1; continue
            if c == '"':
                j = i + 1
                while j < n and t[j] != '"':
                    j += 2 if t[j] == '\\' else 1
                out += [(p, 'string') for p in range(i, j) if ord(t[p]) > 127]
                i = j + 1; continue
            if c == '#':
                i += 1
                if i < n and t[i] in '({[':
                    st.append(('hash', None)); continue
                m = re.match(r'[A-Za-z_][\w-]*', t[i:])
                if m: i += len(m.group()); st.append(('hash', None))
                continue
            i += 1; continue
        # code
        closer = st[-1][1]
        if c == '"':
            j = i + 1
            while j < n and t[j] != '"':
                j += 2 if t[j] == '\\' else 1
            out += [(p, 'string') for p in range(i, j) if ord(t[p]) > 127]
            i = j + 1; continue
        if c == '`':
            m = re.match(r'`+', t[i:]); b = len(m.group())
            if b == 2: i += 2; continue
            j = t.find('`' * b, i + b); j = n if j < 0 else j + b
            out += [(p, 'raw') for p in range(i, j) if ord(t[p]) > 127]
            i = j; continue
        if c in '({':
            st.append(('code', ')' if c == '(' else '}')); i += 1; continue
        if c == '[':
            st.append(('content', None)); i += 1; continue
        if c == '$':
            st.append(('math', None)); i += 1; continue
        if c == closer:
            st.pop(); i += 1; continue
        i += 1
    return [(p, ctx) for p, ctx in out if not allowed(t[p])]

MARKUP = {'—': '---', '–': '--', '…': '...', '≈': 'approx', '→': 'arrow.r', '·': 'dot.c', '×': 'times',
          '≤': 'lt.eq', '≥': 'gt.eq', '≲': 'lt.tilde', '≳': 'gt.tilde', '↦': 'arrow.r.bar', '≪': 'lt.double',
          '≫': 'gt.double', '⟺': 'arrow.l.r.double.long', '≠': 'eq.not', '■': 'square.filled',
          '⟷': 'arrow.l.r.long', '÷': 'div', '✓': 'checkmark', '✗': 'crossmark', '←': 'arrow.l',
          '⟹': 'arrow.r.double.long', '⪰': 'succ.eq', 'λ': 'lambda', 'σ': 'sigma', '∝': 'prop',
          '▷': 'triangle.stroked.r', '⊗': 'times.o', 'ℓ': 'ell', '∈': 'in'}
MATH = {'—': 'dash.em', '–': 'dash.en', '…': 'dots.h', '≈': 'approx', '→': '->', '·': 'dot.c', '×': 'times',
        '≤': '<=', '≥': '>=', '≲': 'lt.tilde', '≳': 'gt.tilde', '↦': '|->', '≪': '<<', '≫': '>>',
        '⟺': '<==>', '≠': '!=', '⟷': '<-->', '÷': 'div', '←': '<-', '⟹': '==>', '⪰': 'succ.eq',
        'λ': 'lambda', 'σ': 'sigma', '∝': 'prop', '⊗': 'times.o', 'ℓ': 'ell', '↔': '<->', '∈': 'in'}
ASCII = {'—': '--', '–': '-', '…': '...', '≈': '~', '→': '->', '·': '.', '×': 'x', '≤': '<=', '≥': '>=',
         '≲': '<~', '≳': '>~', '↦': '|->', '≪': '<<', '≫': '>>', '⟺': '<=>', '≠': '!=', '⟷': '<->',
         '÷': '/', '←': '<-', '⟹': '=>', '∝': '~', 'ℓ': 'l', '↔': '<->', '∈': 'in', 'é': 'e', 'è': 'e',
         'ü': 'u', 'ö': 'o', 'ä': 'a', 'ě': 'e', 'Å': 'A', '½': '1/2', 'λ': 'lambda', 'σ': 'sigma',
         '✓': 'ok', '✗': 'x', '■': '#', '▷': '>', 'ᵀ': '^T', '⊗': '(x)', '⪰': '>='}

def esc(c): return '\\u{%x}' % ord(c)

def replace(t, items):
    res, last = [], 0
    for i, ctx in items:
        c = t[i]
        res.append(t[last:i])
        prev = t[i-1] if i > 0 else ' '
        nxt = t[i+1] if i + 1 < len(t) else ' '
        if ctx == 'markup':
            if c in ('—', '–', '…'):
                r = MARKUP[c]
                # a following '-' or '.' would merge with the shorthand
                if nxt in '-.': r = '#sym.' + {'—': 'dash.em', '–': 'dash.en', '…': 'dots.h'}[c] + ('' if not (nxt.isalnum() or nxt in '.([') else '')
                if nxt in '-.' : r = '#(sym.' + {'—': 'dash.em', '–': 'dash.en', '…': 'dots.h'}[c] + ')'
            elif c in MARKUP:
                r = '#sym.' + MARKUP[c]
                if nxt.isalnum() or nxt in '.([_-': r = '#(sym.' + MARKUP[c] + ')'
            else:
                r = esc(c)
        elif ctx == 'math':
            if c in MATH:
                r = MATH[c]
                if r[0].isalpha() and (prev.isalnum() or prev in ')"'): r = ' ' + r
                if r[-1].isalpha() and (nxt.isalnum() or nxt in '("'): r = r + ' '
            else:
                r = esc(c)
        elif ctx == 'string':
            r = esc(c)
        else:  # raw, comment
            r = ASCII.get(c, '?')
        res.append(r)
        last = i + 1
    res.append(t[last:])
    return ''.join(res)

if __name__ == '__main__':
    apply = '--apply' in sys.argv
    check = '--check' in sys.argv
    files = [f for f in sys.argv[1:] if not f.startswith('--')]
    stats = collections.Counter()
    for f in files:
        t = open(f).read()
        items = scan(t)
        assert len(items) == sum(not allowed(c) for c in t), (f, len(items))
        for i, ctx in items: stats[(ctx, t[i])] += 1
        if apply:
            new = replace(t, items)
            assert all(allowed(c) for c in new), f
            open(f, 'w').write(new)
    for (ctx, c), k in sorted(stats.items()): print(ctx, c, 'U+%04X' % ord(c), k)
    if check and stats:
        print("non-ASCII characters (other than accented letters) found: run python3 tools/deunicode.py --apply <file>")
        sys.exit(1)
