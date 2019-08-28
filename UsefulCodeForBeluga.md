## Useful codes to use for Beluga Cluster ##

### Knowledge of basic Unix/Linux commands are necessary ###
Useful link: http://mally.stanford.edu/~sr/computing/basic-unix.html

If you want to apply for an account, here's a link explaining how:
https://www.computecanada.ca/research-portal/account-management/apply-for-an-account/

Once you get confirmation for your registration (24-48h), here are useful codes to know.

**1. Connect to the cluster**: Use ssh on your terminal (type **command** + **space**,then search for **Terminal**)
<br /> ```ssh username@beluga.computecanada.ca```



*Essentially, compute canada works the same as your own terminal. However, for any commands that would last more than*
<br /> *more than 3 mintutes, you should run a ```sbatch``` job (for more info, see below)*



**2. Which directory should you choose?**
<br /> You should **RUN** your analysis on the scratch directory. This is a temporary directory where every data is erased **every two months** (you will be notified by a week in advance email). 


<br /> **Why using this directory?** This directory have **more storage (20T)** and **is faster** to process-in. When you finish your analysis, you will transfer your files to **your own private directory**.
<br /> ```cd /home/tangsab8/scratch/``` 


<br /> You should **STORE** your outputs on your **private** directory. This directory has access to the privileges your PI 
<br /> might have bought and is under the **project** folder.
<br /> ```cd /home/username/projects/ctb-PI/username/YourProjectDirectory(optional)/```

#3. **How to transfer files on the cluster?**
<br /> **For small files:
<br /> You can use scp command to copy from your own terminal (*you will have to ```exit``` to leave the cluster to do it your own terminal)
