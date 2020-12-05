<h1>ESwarm</h1>

<p><strong>ESwarm</strong> simulates the Particle Swarm Optimization algorithm in Python.</p>

<h3>1. Introduction</h3>

<p><a href="https://en.wikipedia.org/wiki/Particle_swarm_optimization">Particle Swarm Optimization</a>(PSO) is a computational, iterative method that aims to improve the solution to a problem with respect to a given measure of quantity.</p>

<p>It is a biologically inspired optimization method first introduced in a paper by Russel Eberhart and James Kennedy in 1995, for the optimization of nonlinear functions. <br>
DOI: <a href="10.1109/ICNN.1995.488968">10.1109/ICNN.1995.488968</a>
</p>

<p><strong>PSO</strong> simulates the behaviors of bird flocking. Let us assume we have the following scenario: a group of birds are randomly searching food in an area. There is only one piece of food in the area being searched. All the birds do not know where the food is. But they know how far the food is in each iteration. So, the most effective strategy to find the food is to follow the bird which is nearest to the food.</p>

<p><strong>PSO</strong> is initialized with a group of random particles (solutions) and then searches for optima by updating generations. In every iteration, each particle is updated by following two "best" values. The first one is the best solution (fitness) it has achieved so far. (The fitness value is also stored.) This value is called pBest. Another "best" value that is tracked by the particle swarm optimizer is the best value, obtained so far by any particle in the population. This best value is a global best and called gBest.</p>

<h3>2. Pseudo Code</h3>
```
FOR each particle
Initialize particle with random positions
END FOR
DO
FOR each particle
Calculate fitness value
IF the fitness value is better than the particle’s best fitness value (pBest) in history
set current value as the new pBest
END FOR
Choose the particle with the best individual fitness value (pBest) of all the particles as the gBest
FOR each particle
Calculate particle velocity according equation (a)
Update particle position according equation (b)
END FOR
WHILE maximum iterations or minimum error criteria is not attained
END

```