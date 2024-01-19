# Pylint Plugin Loader

Pylint is a great tool that keeps your codebase free from code smells.  However, it is very rigid and there are often edge cases in software development where we do not want to apply a pylint rule to a single class, module, or directory.  Pylint has no built-in way of doing this.

This project shows an example of how you can dynamically add ignore statements to parts of your codebase when running `pylint src`.  

Custom plugins are written in `pylint_plugins`.  Each plugin ignores a single pylint warning and the python class name to determine which classes to disable warnings on.

In the `setup.cfg`, we instruct pylint to include these custom plugins with the `load-plugins=pylint_plugins.duplicate_code` line.  

With this approach, you can make necessary ignore statements to your codebase where pylint may be wrong without needing to cover your code with # ignore comments.

## Try it out
1. Create a conda/mamba environment from `environment.yml` using `conda env create --file=environment.yml`
2. Run `pip install --no-deps -e .`
3. Run `pylint src` 

No duplicate-code warnings will be thrown for the `src.special` submodule, but will be thrown for the `src` module.
