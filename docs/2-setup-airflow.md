# Setup Airflow 

Airflow needs to know where your `airflow_home` directory is. When we run Airflow then it will look for it's configuration files, plugins and workflow code inside that directory.

Airflow home has a default value that doesn't make sense for a development environment. We will use an environmental variable to tell Airflow what's up.

## 1. Get the absolute path to your airflow_home directory

If you are using bash (or similar) you could do this to print out the absolute path.

```
cd src # if you aren't there already

cd airflow_home
pwd
```

Mine looks like this:

```
/home/sheena/workspace/airflow-tutorial/src/airflow_home
```

## 2. Figure out where your activate script is

You can tell Airflow where airflow_home is by exporting an environmental variable like so:

```
export AIRFLOW_HOME=/path/to/your/airflow-tutorial/src/airflow_home
```

But it's a bit of a pain in the neck to have to do that every time you want to do anything Airflow related.  So we'll set up your virtual environment so that it does the export every time we activate it. 

This is just a nice trick to save us from unnecessary suffering as we continue our work. It's not strictly necessary.

If you followed the instructions exactly then there should be a venv directory inside the src directory. Your `activate` script will then be at `src/venv/bin/activate`.  You can move onto step 3.

If you used a different tool to create your virtual environment, or you put your virtual environment somewhere else then your path might be different. 

To find out where your activate script is do the following:

```
# 1. activate your venv then

# 2. Find the path to the Python executable

which python 
```

The Python executable will be inside a directory named `bin`. Your activate script will be there too.

For example, if your Python executable is at `/home/you/workspace/airflow-tutorial/src/venv/bin/python`, then your activate script will be at `/home/you/workspace/airflow-tutorial/src/venv/bin/activate`

## 3. Edit your `activate` script

Now open the activate script with any editor you want. Eg VSCode.

Put the following at the top of your activate script:

```
export AIRFLOW_HOME=/path/to/your/airflow-tutorial/src/airflow_home
```

NOTE: Replace the path above with the actual path to your airflow home directory.

## 4. Check that it worked

Open up a new shell and activate your virtual environment.

Check that the environmental variable is as it should be.

```[bash]
echo $AIRFLOW_HOME
```

This should print out the value you put in your activate script.

## 5. Run airflow

Let's make sure Airflow is set up properly:

Activate your venv if it's not already active, then run:

```
airflow standalone
```

You should see a whole lotta logs. There might be a few warnings but there should be no error messages.

If you look inside your airflow_home directory it'll now be full of stuff. We'll talk about that stuff later :) 

You can now kill this process with Ctrl+C.

## 6. Cleanup

If you are following along with the guided tutorial then it would be good to delete the contents of your airflow_home directory, otherwise you will not be in a good position to take part in the first exercise.