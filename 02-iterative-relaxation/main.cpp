#include "CSRMatrix.h"

#include <iostream>

int main()
{
    auto A = createLaplacian2D<int, double>(9);

    for (int i = 0; i < A.n; i++)
    {
        for (int j = A.row_ptr[i]; j < A.row_ptr[i + 1]; j++)
        {
            std::cout << "A[" << i << "," << A.col_idx[j] << "] = " << A.values[j] << std::endl;
        }
    }

    return 0;
}