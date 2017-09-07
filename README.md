# nci-config-loader
A simple library to handle ini configuration files within your projects

## Usage

Every aspect of the Config class is statically defined; This means that once initiated, the same information is available anywhere within the execution of the program.

### Loading a config file:
```python
if not Config.ready():
  Config.parser.read("config.ini")
```

### Accessing data
Given this config.ini file:
```ini
[GoogleAnalytics]
user : myusername
password : mypassword
...
```

You can access the GoogleAnalytics user in your application using this line:

```python
print(Config.get("GoogleAnalytics")["user"])
```

### Get a Categories
Getting a category without specifying a variable name will return a dictionary; This means that all standard dictionary methods can apply:

* **get values**: ```Config.get("Commands").values() ```
* **get keys**: ```Config.get("Commands").keys() ```



