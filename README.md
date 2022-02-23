# General setting up on MacOS

## Zsh installation

It's recommended to use `Zsh` over `Bash`. Fortunately, Zsh is the default shell in my MacOs.

To check your account's default shell, simply run the following command:

```
echo $SHELL
```

## GCC installation

Python install will require a GCC installation, and Xcode includes command line development tools such as gcc and friends, so we need to install Xcode as follows:

```
xcode-select --install
```

## Homebrew installation

A package manager is missing in MacOS unlike in Linux. Homebrew fills this void.

To install Homebrew, run the following command:

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
> For more details, refer to [this](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-homebrew-on-macos)

## Git and VS Code installation

```
brew install git
```
```
brew install --cask visual-studio-code
```
```
brew doctor
```

# Setting up for the Python development environment

## Pyenv installation

This tool lets us switch easily between multiple versions of Python in our machine.

1. To install it, let's 'brew' as follows:

```
brew install pyenv
```

2. Configure your shell's environment for Pyenv as follows (**zsh** for me):

```
echo '\neval "$(pyenv init --path)"' >> ~/.zprofile
```
```
echo '\neval "$(pyenv init -)"' >> ~/.zshrc
```
>For more details, refer to [this](https://github.com/pyenv/pyenv#basic-github-checkout)

3. Restart terminal windows for changes to take effect


## Python installation

1. Now let's install the latest Python version (3.10.2 as of this writting) using the `pyenv` tool

```
pyenv install 3.10.2
```

2. And then switch current Python version to 3.10.2 as follows:
```
pyenv global 3.10.2
```

>To verify if the current Python version is 3.10.2 or not, run the following command: `pyenv version`

3. To fix `brew doctor`'s warning that is **"config" scripts exist outside your system or Homebrew directories**, add the following line into `~/.zshrc`:

```
alias brew='env PATH="${PATH//$(pyenv root)\/shims:/}" brew'
```
>For more details, refer to [this](https://github.com/pyenv/pyenv#homebrew-in-macos)

# Setting up for this project only

1. Navigate to the directory of this project and then create a new python virtual environment named `venv-py-practice`
```
cd ~/Projects/py-practice
```
```
python -m venv venv-py-practice
```

2. In order to use this environment, we have to 'activate' it, to do this, run the following:
```
source ./venv-py-practice/bin/activate
```
> For more details, refer to [this](https://realpython.com/python-virtual-environments-a-primer/)

3. Install all packages according to the configuration file `requirements.txt`
```
pip install -r requirements.txt
```
> For more details, refer to [this](https://note.nkmk.me/en/python-pip-install-requirements/)


