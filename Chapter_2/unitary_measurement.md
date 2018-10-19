1. How can measurements be expressed as the unitary evolution of a quantum system?

One can take on assumption the presence of a Unitary operator U that acts on the tensor product of a regular quantum state and a fixed state of a measurement operator.

By the completeness relation, the multiplication of the operator U with its adjoint is equivalent to the summation of all measurement operators by their own adjoint.

Since both the unitary operator and measurement operator are defined on measurement/state space tensor products, when we extend the equation to take advantage of the equivalence between the summation of measurement operators and the unitary operators, we need only consider measurement operator multiplied against their own adjoint, in the same measurement space (orthonomality ensures that diverging orthogonal vectors multiply the whole term by 0 - similar ones preserve the term because they're both length 1, and have the same components). By equating the operators to the identity operator, the final equivalence is revealed to be the inner product between two arbitrary state vectors.

An operator defined on a subspace to a vector space can be extended by preserving its W -> V map, and defining the remaining V -> V map in any way it chooses.

2. What is the difference between hermitian and unitary operators?
   Hermitian operators are equal to their self-adjoint, unitary operators equal the identity operator when taken with their self-adjoint. Unitary operators capture the reversability constraint of quantum mechanics. Hermitian operators are not necessarily unitary.

3. How are projective measurements different from general measurements?
   Projective measurements have an additional constraint that the observable's measurement operators must be orthogonal projectors. Apparantly, general measurmenets allow for more continuous measurements, but I need to look into this more. I understand that projective measurements can only measure eigenvalues of an orthonormal eigenvector basis. Also, general measurements are not necessarily repeatable, which models experiements without repeatable results better.

4. Why is it important that postulate 3 can be regained from unitary dynamics, projective measurements, and system conjugation?
   The capacity of general measurements to have non eigenvalue results gives them utility - understanding how projective measurements can be extended to have finer grained control through simple admission of unitary dynamics lends insight into how general measurements "work".

5. How are projective measurements lower level than the general measurements described by postulate 3?
   They need to be extended with unitary transformations. Basically, evolving the tensor of the measurement state with the pure state can give you a finer-tuned mearurement.
