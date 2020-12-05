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
            Set current value as the new pBest
    END FOR
    Choose the particle with the best individual fitness value (pBest) of all the particles as the gBest
    FOR each particle
        Calculate particle velocity according equation (a)
        Update particle position according equation (b)
    END FOR
WHILE maximum iterations or minimum error criteria is not attained
END
```

<h3>3. Directory Structure</h3>

```bash
~root
    ~\Simulations
    <!--Find simulations here-->
    Particle.py
    Run.py
    __init__.py
    pso_config.py
```
```bash
├── Simulations
│   ├── PSO_Run.mp4
│   ├── sim01.png
│   ├── sim09.png
│   ├── sim11.png
│   ├── sim16.png
│   ├── sim20.png
│   ├── sim24.png
│   └── sim28.png
├── __pycache__
├── Particle.py
├── Readme.md
├── Run.py
├── Space.py
├── __init__.py
└── pso_config.py
```

<p>Run the program using <a href="https://github.com/Sohambasu07/ESwarm/blob/master/Run.py">Run.py</a><br>
Change parameter values in <a href="https://github.com/Sohambasu07/ESwarm/blob/master/pso_config.py">pso_config.py</a>
</p>

<h3>4. Simulation Results</h3>

<table>
<tr><td>
<img src="https://github.com/Sohambasu07/ESwarm/blob/master/Simulations/PSO_Run.gif">
</td></tr>
</table>



<table>

<tr>

<td>
<img src="https://github.com/Sohambasu07/ESwarm/blob/master/Simulations/sim01.png">
</td>

<td>
<img src="https://github.com/Sohambasu07/ESwarm/blob/master/Simulations/sim09.png">
</td>

<td>
<img src="https://github.com/Sohambasu07/ESwarm/blob/master/Simulations/sim11.png">
</td>

</tr>

<tr>

<td>
<img src="https://github.com/Sohambasu07/ESwarm/blob/master/Simulations/sim16.png">
</td>

<td>
<img src="https://github.com/Sohambasu07/ESwarm/blob/master/Simulations/sim20.png">
</td>

<td>
<img src="https://github.com/Sohambasu07/ESwarm/blob/master/Simulations/sim24.png">
</td>

</tr>


<tr>

<td>
<img src="https://github.com/Sohambasu07/ESwarm/blob/master/Simulations/sim28.png">
</td>

</tr>


</table>