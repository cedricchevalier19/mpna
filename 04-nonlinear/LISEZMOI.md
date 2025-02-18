# Équation de diffusion non linéaire


## Problème physique: diffusion dans une flamme

On veut calculer la répartition de température transversale dans une flamme (figure [3.32](#c3fig15)). Pour cela on utilise un modèle simple, en supposant que dans la direction transverse (notée ![\bgroup\color{black}$ x$\egroup](img195.png) ) on a des échanges de chaleur uniquement par diffusion et par rayonnement.

**Figure 3.32:** Profil de température transversal dans une flamme

![\includegraphics[width=0.2\paperwidth,keepaspectratio]{CHAP3/flamme}](img1585.png)

Avec ces hypothèses, l'équation de conservation de l'énergie à l'état stationnaire dans la direction ![\bgroup\color{black}$ x$\egroup](img195.png) s'écrit:

$$ \underbrace{-\frac{\partial}{\partial}\left(\lambda\frac{\partial T}{\partial x}\right)}_{\mbox{diffusion}} 
+ \underbrace{\sigma(T^{4}-T_{0}^{4})}_{\mbox{rayonnement}}=\underbrace{Q}_{\mbox{source}}$$

  
Dans ce modèle, l'énergie ![\bgroup\color{black}$ Q$\egroup](img1587.png) produite dans la flamme de largeur ![\bgroup\color{black}$ 2\delta$\egroup](img1461.png) par réaction chimique est diffusée par conduction et rayonné vers l'air extérieur à température ![\bgroup\color{black}$ T_{0}$\egroup](img171.png) . Pour le rayonnement, nous avons adopté un modèle simple de rayonnement de corps noir proportionnel à ![\bgroup\color{black}$ T^{4}$\egroup](img1588.png) avec une constante de rayonnement ![\bgroup\color{black}$ \sigma$\egroup](img1589.png) . Les variations de température entre la flamme et l'extérieur étant importantes (avec un rapport de l'ordre de 3 à 4), le coefficient de conduction ![\bgroup\color{black}$ \lambda$\egroup](img165.png) dépend de la température à travers une loi en puissance ![\bgroup\color{black}$ \lambda(T)=\lambda_{0}T^{q}$\egroup](img1590.png) . Enfin pour le terme source, nous choisirons un terme de réaction constant dans la flamme et nul à l'extérieur.

En supposant que la flamme est symétrique, les conditions aux limites s'écrivent:

![\bgroup\color{black}$\displaystyle \frac{\partial T}{\partial x}(x=0)=0     $\egroup](img1591.png) et ![\bgroup\color{black}$\displaystyle T(x=L)=T_{0}$\egroup](img1592.png)   

 ![\bgroup\color{black}$ L$\egroup](img169.png)étant une distance grande par rapport à l'épaisseur ![\bgroup\color{black}$ \delta$\egroup](img493.png) de la flamme.

En posant ![\bgroup\color{black}$ u=\frac{T}{T_{0}}$\egroup](img1593.png) , le problème modèle associé s'écrit alors (en choisissant ![\bgroup\color{black}$ L=1$\egroup](img529.png) et ![\bgroup\color{black}$ \delta=0,2$\egroup](img1594.png) ):

![$\displaystyle -\frac{\partial}{\partial}\left(\kappa(u)\frac{\partial u}{\partial x}\right)+\sigma(u^{4}-1)=Q(x)       x\in]0,1[$](img1595.png) (3.67)

![$\displaystyle \frac{\partial u}{\partial x}(0)=0 \„      u(1)=1$](img1596.png)

avec ![\bgroup\color{black}$ Q(x)=\beta  Heaviside(0.2-x)$\egroup](img1597.png) et ![\bgroup\color{black}$ \kappa(u)=\kappa_{0}u^{q}$\egroup](img1598.png) .

## Étude analytique
----------------------

Le problème ([3.67](#c3eq51)) étant non linéaire, il n'existe pas de solution analytique simple. Cependant dans le cas de faibles variations de ![\bgroup\color{black}$ u$\egroup](img179.png) ,

![\bgroup\color{black}$\displaystyle u\approx1   \Rightarrow\kappa(u)\approx\kappa_{0} \„  \sigma(u^{4}-1)\approx4\sigma(u-1)$\egroup](img1599.png)

on peut écrire un problème linéaire équivalent (en posant ![\bgroup\color{black}$ \alpha=4\sigma$\egroup](img1600.png) ):

![$\displaystyle -\frac{\partial}{\partial}\left(\kappa_{0}\frac{\partial u}{\partial x}\right)+\alpha(u-1)=Q(x)$](img1601.png) (3.68)

  
On a tracé sur la figure ([3.33](#c3fig16)) cette solution analytique pour ![\bgroup\color{black}$ \kappa_{0}=0,01$\egroup](img1602.png) et différentes valeurs de ![\bgroup\color{black}$ \alpha$\egroup](img994.png) pour montrer l'importance du rayonnement qui a tendance à raidir le front de température.

**Figure 3.33:** solution linéaire de ([3.68](#c3eq52)) pour différentes valeurs de ![$ \alpha $](img60.png) 

![\includegraphics[width=0.2\paperwidth,keepaspectratio]{CHAP3/solflamme}](img1603.png)

## Discrétisation par différences finies
-------------------------------------------

Pour résoudre numériquement le problème non linéaire ([3.67](#c3eq51)), on le discrétise tout d'abord par différences finies centrées avec un maillage de pas ![\bgroup\color{black}$ dx=1/N$\egroup](img1392.png) sous la forme:

![$\displaystyle -\left(\frac{\kappa_{i+\frac{1}{2}}\left(u_{i+1}-u_{i}\right)-\ka...
...ht)}{dx^{2}}\right)+\sigma\left(u_{i}^{4}-1\right)=Q_{i}    \forall i=0,N-1$](img1604.png) (3.69)

en notant ![\bgroup\color{black}$ \kappa_{i+\frac{1}{2}}=\kappa\frac{\kappa(u_{i+1})+\kappa(u_{i})}{2}$\egroup](img1605.png) et ![\bgroup\color{black}$ \kappa_{i-\frac{1}{2}}=\frac{\kappa(u_{i-1})+\kappa(u_{i})}{2}$\egroup](img1606.png) les coefficients de diffusion en ![\bgroup\color{black}$ i+\frac{1}{2}$\egroup](img1607.png) et ![\bgroup\color{black}$ i-\frac{1}{2}$\egroup](img1608.png) .

A ces équations on ajoute les 2 conditions aux limites:

1.  la condition de Neumann en ![$ i=0$](img554.png) , traduite comme une condition miroir pour l'équation en ![$ i=0$](img554.png) :  ![$ u_{-1}=u_{1}$](img1609.png) ,
2.  la condition de Dirichlet en ![$ i=N$](img1610.png) : ![$ u_{N}=1$](img1611.png) .

On obtiens ainsi ![\bgroup\color{black}$ N+1$\egroup](img469.png) équations non linéaires pour ![\bgroup\color{black}$ N+1$\egroup](img469.png) inconnues ![\bgroup\color{black}$ \{u_{i}\}_{i=0,N}$\egroup](img1612.png) , que l'on écrit symboliquement sous la forme:

![$\displaystyle F_{i}(u_{0},u_{1},..u_{j}...,u_{N})=0     \forall i=0,N$](img1613.png) (3.70)


Pour résoudre numériquement ces équations, on transforme le problème en un problème équivalent de point fixe (i.e. ayant la même solution que [3.70](#c3eq54)):

![$\displaystyle u_{i}=G_{i}(u_{0},u_{1},..u_{j}...,u_{N})     \forall i=0,N$](img1614.png) (3.71)

  
A partir de ce système ([3.71](#c3eq55)), on construit une suite de valeurs ![\bgroup\color{black}$ \{u_{i}^{k}\}_{i=0,N}$\egroup](img1615.png) telle que:

![$\displaystyle u_{i}^{k+1}=G_{i}(u_{0}^{k},u_{1}^{k},..u_{j}^{k}...,u_{N}^{k})   \forall i=1,N$](img1616.png) (3.72)

  
Si la suite ![\bgroup\color{black}$ \{u_{i}^{k}\}_{i=0,N}$\egroup](img1615.png) converge, elle converge vers un point fixe (i.e. une solution) de ([3.71](#c3eq55)) et donc vers la solution du problème non linéaire initial ([3.70](#c3eq54)). La condition de convergence de la suite de point fixe ([3.72](#c3eq56)) est donnée par le théorème classique du point fixe:

**théorème du point fixe:**

la suite itérative ([3.72](#c3eq56)) converge au voisinage d'un point fixe de ([3.71](#c3eq55)) si et seulement si la matrice jacobienne ![$ J$](img1617.png) de ![$ G$](img917.png) :  ![$ J_{i,j}=\left(\frac{\partial G_{i}}{\partial u_{j}}\right)$](img1618.png) , a une norme inférieure à 1, i.e. possède dans ce voisinage des valeurs propres de modules inférieurs à 1.

  
## Schéma explicite
-------------------------

Une première approche consiste à considérer la solution du problème initial ([3.67](#c3eq51)) comme solution stationnaire du problème instationnaire associé:

![$\displaystyle \frac{\partial u}{\partial t}-\frac{\partial}{\partial}\left(\kappa(u)\frac{\partial u}{\partial x}\right)+\sigma(u^{4}-1)=Q(x)$](img1619.png) (3.73)

  

On discrétise cette équation avec du schéma différences finies explicite en temps:

![$\displaystyle \frac{u_{i}^{n+1}-u_{i}^{n}}{dt}-\left(\frac{\kappa_{i+\frac{1}{2...
...n}\right)}{dx^{2}}\right)+\sigma\left(\left(u_{i}^{n}\right)^{4}-1\right)=Q_{i}$](img1620.png) (3.74)

  

Ce schéma explicite s'écrit s'écrit sous la forme d'un problème de point fixe:

![\bgroup\color{black}$\displaystyle u_{i}^{n+1}=G_{i}(u_{0}^{n}..u_{N}^{n})$\egroup](img1621.png)

avec

![$\displaystyle G_{i}$](img1622.png)

![$\displaystyle =$](img241.png)

![$\displaystyle u_{i}^{n}+dt\left(\frac{\kappa_{i+\frac{1}{2}}^{n}\left(u_{i+1}^{...
...t)-\kappa_{i-\frac{1}{2}}^{n}\left(u_{i}^{n}-u_{i-1}^{n}\right)}{dx^{2}}\right)$](img1623.png) (3.75)


![$\displaystyle -$](img367.png)

![$\displaystyle dt \sigma\left(\left(u_{i}^{n}\right)^{4}-1\right)+dt  Q_{i}$](img1624.png)


La matrice jacobienne ![\bgroup\color{black}$ \mathcal{G}$\egroup](img1625.png) de ![\bgroup\color{black}$ G$\egroup](img1106.png) est la matrice tridiagonale d'ordre ![\bgroup\color{black}$ N+1$\egroup](img469.png) suivante:

![\bgroup\color{black}$\displaystyle \mathcal{G}=\left[\begin{array}{cccccc}
a_{0}...
... 0 & \ddots & a_{N-1} & b_{N-1}\\
0 & 0 & 0 & & 0 & 0\end{array}\right]$\egroup](img1626.png)

avec

![$\displaystyle a_{i}$](img1627.png)

![$\displaystyle =$](img241.png)

![$\displaystyle 1-dt\left(\frac{\kappa_{i+\frac{1}{2}}^{n}+\kappa_{i-\frac{1}{2}}...
...{n}-u_{i-1}^{n}-u_{i+1}^{n})}{dx^{2}}+4\sigma\left(u_{i}^{n}\right)^{3}\right),$](img1628.png)
 

![$\displaystyle b_{i}$](img1629.png)

![$\displaystyle =$](img241.png)

![$\displaystyle   dt \frac{\kappa_{i+\frac{1}{2}+}^{n}}{dx^{2}}+\frac{\frac{1}{2}(\frac{\partial\kappa_{i+1}}{\partial u_{i+1}})(u_{i+1}^{n}-u_{i}^{n})}{dx^{2}}$](img1630.png)
 

![$\displaystyle c_{i}$](img1631.png)

![$\displaystyle =$](img241.png)

![$\displaystyle dt \frac{\kappa_{i-\frac{1}{2}}^{n}}{dx^{2}}+\frac{\frac{1}{2}(\frac{\partial\kappa_{i-1}}{\partial u_{i-1}})(u_{i-1}^{n}-u_{i}^{n})}{dx^{2}}$](img1632.png)
 
Par définition, cette matrice Jacobienne relie une petite variation ![\bgroup\color{black}$ \delta u_{i}^{n}$\egroup](img1633.png) de la solution à l'étape ![\bgroup\color{black}$ n$\egroup](img237.png) à la variation correspondante ![\bgroup\color{black}$ \delta u_{i}^{n+1}$\egroup](img1634.png) à l'étape ![\bgroup\color{black}$ n+1$\egroup](img426.png) :

![\bgroup\color{black}$\displaystyle \left[\delta u_{i}^{n+1}\right]=\mathcal{G}\left[\delta u_{i}^{n}\right]$\egroup](img1635.png)

En interprétant ![\bgroup\color{black}$ \delta u_{i}^{n}$\egroup](img1633.png) comme une perturbation, la relation précédente montre que la matrice ![\bgroup\color{black}$ \mathcal{G}$\egroup](img1625.png) est la matrice d'amplification du schéma différences finies explicite ([3.74](#c3eq59)), i.e. une perturbation ![\bgroup\color{black}$ \epsilon_{i}^{n}$\egroup](img427.png) de la solution de ([3.73](#c3eq57)) vérifie

![\bgroup\color{black}$\displaystyle \left[\epsilon_{i}^{n+1}\right]=\mathcal{G}\left[\epsilon_{i}^{n}\right]$\egroup](img1636.png)

Or pour que le schéma ([3.74](#c3eq59)) soit stable, il faut que les valeurs propres de la matrice ![\bgroup\color{black}$ \mathcal{G}$\egroup](img1625.png) soient en module inférieures à 1. Pour notre schéma, la condition de convergence de la méthode de point fixe est en faite une condition de stabilité sur le schéma explicite associé.

Pour pouvoir faire l'analyse simplement, on simplifie les coefficients de la matrice ![\bgroup\color{black}$ \mathcal{G}$\egroup](img1625.png) en négligeant les termes en ![\bgroup\color{black}$ \frac{1}{2}(\frac{\partial\kappa_{i}}{\partial u_{i}})$\egroup](img1637.png) devant ceux en ![\bgroup\color{black}$ \kappa_{i}$\egroup](img1638.png) :

![\bgroup\color{black}$\displaystyle a_{i}\approx1-dt\left(\frac{\kappa_{i+\frac{1...
...{dx^{2}},   c_{i}\approx dt \frac{\kappa_{i-\frac{1}{2}}^{n}}{dx^{2}}$\egroup](img1639.png)

L'équation sur la perturbation ![\bgroup\color{black}$ \epsilon_{i}^{n}$\egroup](img427.png) s'écrit alors:

![\bgroup\color{black}$\displaystyle \frac{\epsilon_{i}^{n+1}-\epsilon_{i}^{n}}{dt...
...silon_{i-1}^{n}\right)}{dx^{2}}+4\sigma(u_{i}^{n})^{3}\epsilon_{i}^{n}=0$\egroup](img1640.png)

Cette équation est analogue à l'équation de la perturbation du schéma explicite pour le problème de convection linéaire étudié au paragraphe (c3chalsource) avec les paramètres ![\bgroup\color{black}$ \kappa=\kappa_{i+\frac{1}{2}}=\kappa_{i-\frac{1}{2}}$\egroup](img1641.png) et ![\bgroup\color{black}$ \alpha=4\sigma(u_{i}^{n})^{3}$\egroup](img1642.png) .

L'étude de stabilité à été faîte au paragraphe [3.2.4](node24.html#c3chalexp) pour ce schéma explicite linéaire, et on a trouvé une condition de stabilité donnée par la relation ([3.7](node24.html#c3eq4)).

Par analogie, la condition de stabilité pour le schéma explicite non linéaire ([3.75](#c3eq58)) s'écrit donc:

![\bgroup\color{black}$\displaystyle dt<\frac{2}{4\sigma\left(u_{i}^{n}\right)^{3}+\frac{4\kappa(u_{i}^{n})}{dx^{2}}}$\egroup](img1643.png)

Contrairement au cas linéaire, cette condition dépend de la solution ![\bgroup\color{black}$ u_{i}^{n}$\egroup](img400.png) . En notant ![\bgroup\color{black}$ u_{max}=Max(\vert u_{i}^{n}\vert)$\egroup](img1644.png) , la valeur maximale de la solution à l'étape ![\bgroup\color{black}$ n$\egroup](img237.png) , on choisit le pas en temps ![\bgroup\color{black}$ dt$\egroup](img536.png) à l'étape ![\bgroup\color{black}$ n$\egroup](img237.png) tel que:

![$\displaystyle dt<\frac{2}{4\sigma u_{max}^{3}+\frac{4\kappa(u_{max})}{dx^{2}}}$](img1645.png) (3.76)

  

Le schéma explicite converge pour de très petites valeurs du pas en temps, vérifiant la condition ([3.76](#c3eq62)). Cette condition devient très sévère lorsque le nombre de points de calcul ![\bgroup\color{black}$ N$\egroup](img295.png) augmente (i.e. lorsque ![\bgroup\color{black}$ dx$\egroup](img1046.png) diminue).

## Schéma implicite linéarisé

Pour améliorer la convergence, on peut utiliser un schéma implicite linéarisé, basé sur le schéma implicite linéaire ([3.5](node24.html#c3eq2)) avec ![\bgroup\color{black}$ \theta=1$\egroup](img1095.png) .

![$\displaystyle \frac{u_{i}^{n+1}-u_{i}^{n}}{dt}-\left(\frac{\kappa_{i+\frac{1}{2...
...dx^{2}}\right)+\sigma\left(u_{i}^{n+1}\left(u_{i}^{n}\right)^{3}-1\right)=Q_{i}$](img1646.png) (3.77)

  

Ce schéma s'écrit aussi sous la forme d'une itération de point fixe:

![$\displaystyle \left[u_{i}^{n+1}\right]=\mathcal{A}^{-1}\left[u_{i}^{n}+dt (Q_{i}+\sigma)\right]$](img1647.png) (3.78)

  

où ![\bgroup\color{black}$ \mathcal{A}$\egroup](img1157.png) est la matrice tridiagonale d'ordre ![\bgroup\color{black}$ N+1$\egroup](img469.png) suivante:

![\bgroup\color{black}$\displaystyle \mathcal{A}=\left[\begin{array}{cccccc}
a_{0}...
... 0 & \ddots & a_{N-1} & b_{N-1}\\
0 & 0 & 0 & & 0 & 1\end{array}\right]$\egroup](img1648.png)

avec

![\bgroup\color{black}$\displaystyle a_{i}=1+dt\left(\frac{\kappa_{i+\frac{1}{2}}^...
...2}}^{n}}{dx^{2}},   c_{i}=-dt\frac{\kappa_{i-\frac{1}{2}}^{n}}{dx^{2}}$\egroup](img1649.png)

La convergence de l'itération de point fixe ([3.78](#c3eq64)) est lié à la stabilité du schéma ([3.77](#c3eq63)). La matrice Jacobienne ![\bgroup\color{black}$ \mathcal{G}$\egroup](img1625.png) de l'itération de point fixe s'écrit:

![\bgroup\color{black}$\displaystyle \mathcal{G}_{i,j}=\left[\mathcal{A}_{i,j}+\frac{\partial\mathcal{A}_{i,j}}{\partial u_{k}}u_{k}^{n}\right]^{-1}$\egroup](img1650.png)

Dans le cas linéaire, la matrice ![\bgroup\color{black}$ \mathcal{A}$\egroup](img1157.png) est constante, et on a ![\bgroup\color{black}$ \mathcal{G}=\mathcal{A}^{-1}$\egroup](img1651.png) . On a montré au paragraphe c3chalimp que le schéma implicite linéaire est inconditionnellement stable, et donc que la matrice ![\bgroup\color{black}$ \mathcal{A}^{-1}$\egroup](img1652.png) possède des valeurs propres de module inférieur à 1. Dans la cas non linéaire, il faut faire intervenir la dérivée des coefficients de ![\bgroup\color{black}$ \mathcal{A}$\egroup](img1157.png) par rapport à la solution ![\bgroup\color{black}$ u_{i}^{n}$\egroup](img400.png) . La matrice ![\bgroup\color{black}$ \frac{\partial\mathcal{A}}{\partial u_{k}}u_{k}^{n}$\egroup](img1653.png) étant proportionnelle à ![\bgroup\color{black}$ dt$\egroup](img536.png) , pour des petits pas en temps on a ![\bgroup\color{black}$ \mathcal{G\approx A}^{-1}$\egroup](img1654.png) , et l'itération de point fixe converge puisque les valeurs propres de ![\bgroup\color{black}$ \mathcal{A}^{-1}$\egroup](img1652.png) sont en module plus petites que 1.

On peut donc en conclure que le schéma implicite linéarisé converge pour des petits pas en temps. Cependant la limite de convergence est beaucoup plus grande que pour le schéma explicite, et on a un schéma plus efficace.

## Schéma de Newton
----------------------

Pour rechercher les racines des équations non linéaires ([3.70](#c3eq54)), on peut utiliser la méthode de Newton-Raphson, qui consiste à construite la suite itérative de point fixe suivante:

![$\displaystyle \left[u_{i}^{k+1}\right]=\left[u_{i}^{k}\right]-\left[\mathbf{J}^{k}\right]_{i,j}^{-1}\left[F_{j}(u_{0}^{k},..u_{N}^{k})\right]$](img1655.png) (3.79)

  

 ![\bgroup\color{black}$ \mathbf{J}^{k}$\egroup](img1656.png)est la matrice jacobienne des fonctions ![\bgroup\color{black}$ F_{i}$\egroup](img1657.png) : ![\bgroup\color{black}$ \mathbf{J}_{i,j}^{k}=\frac{\partial F_{i}}{\partial u_{j}}(u_{0}^{k}..u_{N}^{k})$\egroup](img1658.png) calculée à l'itération ![\bgroup\color{black}$ k$\egroup](img280.png) . Cette relation s'écrit sous la forme matricielle:

![$\displaystyle \mathbf{J}^{k}\left[u_{i}^{k+1}-u_{i}^{k}\right]=-\left[F_{j}(u_{0}^{k},..u_{N}^{k})\right]$](img1659.png) (3.80)

  

A chaque itération de Newton, il faut résoudre un système linéaire d'ordre ![\bgroup\color{black}$ N+1$\egroup](img469.png) .

Dans notre cas, la matrice Jacobienne ![\bgroup\color{black}$ \mathbf{J}^{k}$\egroup](img1656.png) est tridiagonale et s'écrit:

![\bgroup\color{black}$\displaystyle \mathbf{J}^{k}=\left[\begin{array}{cccccc}
a_...
... 0 & \ddots & a_{N-1} & b_{N-1}\\
0 & 0 & 0 & & 0 & 1\end{array}\right]$\egroup](img1660.png)

avec:

  

![$\displaystyle a_{i}$](img1627.png)

![$\displaystyle =$](img241.png)

![$\displaystyle \left(\frac{\kappa_{i+\frac{1}{2}}+\kappa_{i-\frac{1}{2}}}{dx^{2}...
...{n}-u_{i-1}^{n}-u_{i+1}^{n})}{dx^{2}}+4\sigma\left(u_{i}^{k}\right)^{3}\right),$](img1661.png)

 

![$\displaystyle b_{i}$](img1629.png)

![$\displaystyle =$](img241.png)

![$\displaystyle -\frac{\kappa_{i+\frac{1}{2}}}{dx^{2}}-\frac{\frac{1}{2}(\frac{\partial\kappa_{i+1}}{\partial u_{i+1}})(u_{i+1}^{n}-u_{i}^{n})}{dx^{2}},$](img1662.png)

 

![$\displaystyle c_{i}$](img1631.png)

![$\displaystyle =$](img241.png)

![$\displaystyle -\frac{\kappa_{i-\frac{1}{2}}}{dx^{2}}-\frac{\frac{1}{2}(\frac{\partial\kappa_{i-1}}{\partial u_{i-1}})(u_{i-1}^{n}-u_{i}^{n})}{dx^{2}}.$](img1663.png)
 

Comme pour le schéma explicite, on peut simplifier la calcul de ces coefficients en en négligeant les termes en ![\bgroup\color{black}$ \frac{1}{2}(\frac{\partial\kappa_{i}}{\partial u_{i}})$\egroup](img1637.png) devant ceux en ![\bgroup\color{black}$ \kappa_{i}$\egroup](img1638.png) , ce qui donne:

![$\displaystyle a_{i}\approx\left(\frac{\kappa_{i+\frac{1}{2}}^{n}+\kappa_{i-\fra...
...1}{2}}^{n}}{dx^{2}},   c_{i}\approx-\frac{\kappa_{i-\frac{1}{2}}^{n}}{dx^{2}}$](img1664.png) (3.81)

  

La méthode de Newton converge au voisinage de la racine ![\bgroup\color{black}$ u^{*}$\egroup](img1665.png) . En effet la fonction de point fixe ![\bgroup\color{black}$ G_{i}$\egroup](img1666.png) associée s'écrit:

![\bgroup\color{black}$\displaystyle G_{i}(u_{0},..u_{N})=u_{i}-\left[\mathbf{J}\right]_{i,j}^{-1}\left[F_{j}(u_{0},..u_{N})\right]$\egroup](img1667.png)

et sa matrice Jacobienne ![\bgroup\color{black}$ \mathcal{G}$\egroup](img1625.png) vaut:

![$\displaystyle \left[\mathcal{G}\right]$](img1668.png)

![$\displaystyle =$](img241.png)

![$\displaystyle \left[I_{d}\right]-\left[\mathbf{J}\right]_{i,j}^{-1}\underbrace{...
...\left(\left[\mathbf{J}\right]\right)_{ij}^{-1}\left[F_{j}(u_{0},..u_{N})\right]$](img1669.png)
 

![$\displaystyle =-$](img1670.png)

![$\displaystyle \frac{\partial}{\partial u_{i}}\left(\left[\mathbf{J}\right]\right)_{ij}^{-1}\left[F_{j}(u_{0},..u_{N})\right]$](img1671.png)
 
  

Cette matrice Jacobienne est identiquement nulle en ![\bgroup\color{black}$ u=u^{*}$\egroup](img1672.png) car ![\bgroup\color{black}$ F_{j}(u_{0}^{*},..,u_{N}^{*})=0$\egroup](img1673.png) . Donc sa norme vaut zéro à la racine, et la méthode de Newton converge au voisinage de cette racine.

Cette méthode de point fixe converge au voisinage de la racine (à condition que la racine soit une racine simple), et possède une vitesse de convergence quadratique. C'est la méthode la plus efficace.

