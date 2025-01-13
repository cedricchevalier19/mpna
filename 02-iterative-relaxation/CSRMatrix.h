//
// Simple class for a sparse matrix in CSR format

#ifndef CSRMATRIX_H
#define CSRMATRIX_H

#include <vector>

template <typename IdType, typename ScalarType>
struct CSRMatrix
{
    IdType n;
    std::vector<IdType> row_ptr;
    std::vector<IdType> col_idx;
    std::vector<ScalarType> values;

    CSRMatrix(): n(0)
    {
        row_ptr.push_back(0);
    }

    CSRMatrix(IdType n, int nnz)
        : n(n)
    {
        row_ptr.resize(n + 1);
        col_idx.resize(nnz);
        values.resize(nnz);
    }
};


#endif //CSRMATRIX_H
