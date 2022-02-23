# Setup

## GCC installation

Python install will require a GCC installation, and Xcode includes command line development tools such as gcc and friends, so we need to install Xcode as follows:

```
$ xcode-select --install
```

## Homebrew installation

A package manager is missing in MacOS unlike in Linux. Homebrew fills this void.

To install Homebrew, run the following command:

```
$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

## pyenv installation

This tool lets us switch easily between multiple versions of Python in our machine.

To install it, let's 'brew' as follows:

```
$ brew install pyenv
```

## Python installation

Now let's install the latest Python version (3.10.2 as of this writting) using the pyenv tool

```
$ pyenv install 3.10.2
```

And then switch current Python version to 3.10.2 as follows:
```
$ pyenv global 3.10.2
```

To verify if the current Python version is 3.10.2 or not, run the following command:

```
$ pyenv version
```




