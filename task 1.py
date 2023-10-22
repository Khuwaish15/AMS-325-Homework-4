import numpy as np

# Define the adjacency matrix A
A = np.array([[0, 1, 1, 0, 0, 0],
              [0, 0, 1, 1, 0, 0],
              [1, 0, 0, 0, 0, 0],
              [0, 1, 0, 0, 1, 0],
              [0, 1, 0, 1, 0, 1],
              [0, 0, 0, 0, 1, 0]])

# Step 1: Normalize the columns of A to create matrix M
M = A / np.sum(A, axis=0)
print("Normalized Transition Matrix M:")
print(M)

# Step 2: PageRank Iteration
damping_factor = 0.85
num_pages = 6
threshold = 1e-6
r = np.ones(num_pages) / num_pages  # Initialize the rank vector
s = np.ones(num_pages) / num_pages  # Vector of size 6 with all entries equal to 1/6

converged = False
iteration = 0

while not converged:
    r_new = damping_factor * M.dot(r) + (1 - damping_factor) * s  # PageRank update formula
    if np.linalg.norm(r_new - r) < threshold:
        converged = True
    r = r_new
    iteration += 1
    
# Print PageRank values for each iteration
    print("Iteration", iteration, "PageRank:", r)
    
print("Final PageRank after", iteration, "iterations:", r)




# Step 3: Analyze the results
# We'll calculate the principal eigenvector of M
eigenvalues, eigenvectors = np.linalg.eig(M)
principal_eigenvector = eigenvectors[:, np.argmax(eigenvalues)]
principal_eigenvector = principal_eigenvector / np.sum(principal_eigenvector)

# Compare PageRank with the principal eigenvector
print("Principal Eigenvector of M (normalized):", principal_eigenvector)

# Verify if the PageRank matches the principal eigenvector (for α = 1, they should match)
alpha = 1
if alpha == 1:
    print("Matching PageRank and Principal Eigenvector:", np.allclose(r, principal_eigenvector))


