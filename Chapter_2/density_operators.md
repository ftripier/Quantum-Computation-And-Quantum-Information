Density Operators are another formulation of quantum mechanics, mathematically equivalent to the state vector formulation.

1.  If there's an equivalent formulation, why are density operators taught?
    It provides a much more convenient language for certain commonly encountered scenarios in quantum mechanics. In particular, and relevant to quantum computation, mixed states can model receiving a pure state with noise, where one is uncertain over which pure state it is.

    1.  What are these scenarios?
        Among others, the description of inidividual subsystems of a composite quantum system.

            1. How is the density operator more convenient for talking about them?

2.  In what ways are density operators different from state vectors?
    One definition of density operators describes it as a summation of an outer product of component pure states multiplied by probability coefficients that sum to one.

    1. Why the outer product and not just the pure state?
       Because the density operator is an operator and must map states to states.

    2. Do the states really have to be pure?
       No, because the mixed operator can describe the evolution of states through time through the application of other unitary operators.

    3. How does this operator capture all of quantum mechanics?
       The operator can describe the unitary evolution of a mixed state whereby the operator is extended to have the outer product of the pure state replaced with an outer product of the pure state developed by a unitary operator.

3.  How can density operators describe measurements?
    By equating measurement operations with a summation of the probability of measuring a certain value given a certain state, one regains the density operator (the probability of measuring a certain value given a certain state is equivalent to the trace of multiplying the measurement and its conjugate to the state's projector, because the diagonalization of a stochastic matrix must be one, thereby explaining the trace - this, multiplied by the probability p is equivalent to the density operator).

4.  How can density operators be described without relying on state vectors?
    If you formulate density operators as positive oprators as a trace of 1, you can regain the original postulates of quantum mechanics.

```
2.71 Let p be a density operator. Show that tr(p**2) <= 1, with equality if and only if p is a pure state.

If p is a pure state, then it will have one projector component with coefficient one, and therefore a trace where the diagnol has only one component of value 1 in it. When multiplied by itself, this diagnol will be conserved (and therefore the trace) by definition of  matrix multiplication.
```

5. How can one see if two sets of vector-probability ensembles generate the same density matrix?
   There must be a unitary matrix from one ensemble to the other (that also pads the lower dimensional vector with zero). The proof follows from assuming the theorem above, and applying equational reasoning to a summation of outer products from vectors drawn from both ensembles. The unitary matrix coefficient ends up collapsing into a kroenecker coefficient over the indiciis, which makes them equivalent summations. This collapsing works by the fact that only unitary/co-unitary coefficient products on similar index combinations must have nonzero values, or else they wouldn't equal the identity operator.

6. How can density operators be useful in describing subsystems of entangled systems?
   There exists a _reduced density operator_, which, when applied to a tensor product of two state spaces, acts as a density operator for one of them. It works by multiplying the trace of an outer product from the system it excludes to an outer product of the system it includes. In other words, the reduced density operator takes the partial trace of two tensor'd density operators from seperate state spaces. The physical motivation is purely theoretical - the partial trace is the only operator map which can provide the statistics of measurement for entangled systems that we observe.

   The intuition for the role of the trace comes from the fact that the trace of a measurement applied to a density operator

7. How can the reduced density operator be applied to quantify how much information is known before a quantum teleportation result is classically communicated?
   By applying the reduced density operator to the unmeasured system (entangled with the measured system), one sees that the unmeasured system retains it's complete ambivalence (I/2, or 50% chance of being down, 50% chance of being up).

8. What is schmidt decomposition and why is it useful?
   Schimdt decomposition is an expression of a pure state of a composite system as a summation of a set of positive, nonnegative real number with the tensor product of a vectors drawn from a set of orthonormal bases for each individual system. Schmidt decompositions are useful because they prove algebraic invariants based on decomposing a composite system - things like, if there exists a schmidt decomposition then both component systems must have the same eigenvalues (the schmidt coefficients). This is proved by expressing a pure state of the composite system as the result of a complex matrix applied to the tensor of two vectors drawn from fixed orthonormal bases of each component system. The matrix, with singular value decomposition applied, becomes udv, where u and v are unitary matrices, and d is a non-negative diagonal matrix. the unitary matrices evolve the orthonormal bases to the pure state, and the diagonal elements represent the schmidt coefficients. If the component systems have different dimensionality, the smaller system can be trivially padded, since shmidt coefficients can be zero. Pure states of triple-composite systems cannot be schmidt-decomposed by counting argument - the schmidt decomposition sums over the highest dimensionality system, which isn't necessarily as large as the tensor products dimensionality. a state of a composite system is only a product state if the schmidt coefficient is one, because by definition a product state must be expressed as seperable components across a signle tensor product - if more than one tensor summation is required then it would be invalid.

9. What is purification and why is it useful?
   Purification is an equational process wherein one takes the tensor product of a density operator's orthogonal basis with a reference basis that produces a pure state in the composite system whereby the original measurement (modified to accomodate the composite state space) measure the original system's states with the same probability.
