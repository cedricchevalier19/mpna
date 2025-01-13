#include <iostream>

#include "CSRMatrix.h"
#include "Jacobi.h"

int main()
{
    auto A = createLaplacian2D<int, double>(9);

    std::vector<double> b(A.n, 1.0);
    std::vector<double> x(A.n, 0.0);

    int max_iter = 1000;
    double tolerance = 1e-6;

    auto iter = jacobi(A.n, A, b, x, tolerance, max_iter);

    std::cout << "Number of iterations: " << iter << std::endl;

    std::cout << "Solution:" << std::endl;
    for (int i = 0; i < A.n; ++i)
    {
        std::cout << x[i] << std::endl;
    }

    return 0;
}