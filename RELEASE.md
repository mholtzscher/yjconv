1. Bump version for release

`poetry run bumpversion patch` OR `poetry run bumpversion minor`

1. Release artifacts to PyPi

`poetry publich --build`

1. Push tags

`git push --tags`