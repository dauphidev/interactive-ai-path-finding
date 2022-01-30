# interactive-ai-search-algorithms
An interactive 2D grid visualization for AI **path finding** algorithms. 

## How does it work? 🖱️
* Draw obstacles by holding left click.
* Run the path finding algorithm by right clicking.
* Reset obstacles/search results with a mouse middle click.

## Running the application
You will need Python 3.x installed in your machine and [pygame](https://www.pygame.org).<br>
To install pygame, simply run the following command: `pip install pygame`<br>
To run the application: `python3 engine.py` (linux) or `py engine.py` (windows)

## Currently implemented algorithms:
- [x] Uniform Cost Search (UCS) ---- check point one of the bottom list
- [x] A*

## Bugs/Missing features
- [ ] Adding button to change algorithms. Right now it is needed to manually go to engine.py code and change it. [1]
- [ ] Replacing the right/middle click features with buttons that the user can click in the interface.
- [ ] After a search is completed, show in depth statistics (e.g: maximum frontier size, total cost...)



