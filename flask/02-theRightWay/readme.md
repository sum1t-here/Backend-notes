- Create a virtual env

```python
python3 -m venv flask001
```

- activate the virtual env

```python
source flask001/bin/activate
```

- Install flask

```python
 pip install flask
```

- ```python
    pip freeze > requirment.txt
  ```

Running pip freeze > requirements.txt in your terminal or command prompt will create a file named requirements.txt containing a list of all installed Python packages and their versions. This file is commonly used in Python projects to specify dependencies.

Here's what each part of the command does:

pip freeze: This command generates a list of installed Python packages along with their version numbers.
`>:`This is a redirection operator that directs the output of the pip freeze command to a file.
requirements.txt: This is the name of the file where the output of pip freeze will be stored. This file conventionally contains a list of dependencies required for a Python project.
After running this command, you'll have a requirements.txt file in your current directory containing the list of packages and their versions. You can then use this file to install the same set of packages in another environment by running pip install -r requirements.txt.

```

```
