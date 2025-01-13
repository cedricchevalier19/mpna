#include "CSRMatrix.h"

#include <iostream>

int main()
{
    CSRMatrix<int, double> A(3, 3);
    A.row_ptr = {0, 1, 2, 3};
    A.col_idx = {0, 1, 2};
    A.values = {1.0, 2.0, 3.0};

    for (int i = 0; i < A.n; i++)
    {
        for (int j = A.row_ptr[i]; j < A.row_ptr[i + 1]; j++)
        {
            std::cout << "A[" << i << "," << A.col_idx[j] << "] = " << A.values[j] << std::endl;
        }
    }

    return 0;
}