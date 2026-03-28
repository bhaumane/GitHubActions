# GitHub Actions Information

## Variable and Secret in GitHub Actions workflow

### Using variables in GH Actions
---
**variables for single workflow**:

Define it using the 'env' key in the workflow file. 
The scope of custome variable set by this method is limited to the element in which it is defined.
You can define variables that are scoped for:
- The entire workflow, by using 'env' at the top level of the workflow file
- The content of a job within a workflow
- A spacific step within a job

---

**Configuration variables for Multiple Workflow**:

You can create configuration variables for use across multiple workflows, and can define them at either the organization, repository or environment level.

---

**Context variables from GitHub Metadata**

Contexts are a way to access information about workflow runs, variables, runner environments, jobs, and steps.
For more details about context variables refere below link:

https://docs.github.com/en/actions/reference/workflows-and-actions/contexts#available-contexts

---

**Input for manually triggered workflow**

When using the workflow_dispatch event, you can optionally spacify inputs that are passed to the workflow.

---

**Secrate variables**

Secrate variables are a powerful feature in GitHub Actions that allow you to store sensitive information, such as API keys, passwords, or any other confidential data, securely within your repository. 
They can be used in your workflows without exposing the actual values in your code.
Secret variables are encrypted and can only be accessed by workflows that have been granted permission to use them.

https://docs.github.com/en/actions/reference/workflows-and-actions/contexts#secrets-context

---

## Runners in GitHub Actions

In GitHub Actions, a runner is the server or machine that executes the jobs in a workflow. Runners can be either GitHub-hosted, managed entirely by GitHub, or self-hosted, managed by the user on their own infrastructure.

### Types of Runners:

**GitHub-hosted Runners**: 

These are virtual machines (VMs) hosted by GitHub that come pre-installed with the runner application and a variety of tools, packages, and settings.

**Management**: GitHub handles all maintenance and upgrades of the machines.

**Operating Systems**: Available with Ubuntu Linux, Windows, and macOS operating systems.

**Ephemerality**: Each job runs in a fresh, newly-provisioned VM instance, which is decommissioned after the job finishes, providing a clean environment and enhanced security.

**Cost**: Standard runners are free for public repositories; private repositories get a free minute quota, then are charged based on usage. Larger runners with more resources (CPU, RAM, GPU) are also available at a cost.

**Self-hosted Runners**: 

These are physical, virtual, or containerized systems that you deploy and manage to run jobs from GitHub Actions.

**Control**: You have more control over the hardware, operating system, and software environment, allowing for custom configurations (e.g., specific hardware, local network access).

**Responsibility**: You are responsible for the costs and maintenance of the runner machines, including operating system and software updates (the runner application itself can update automatically).

**Placement**: Can be added at the repository, organization, or enterprise level.

**Cost**: Free to use with GitHub Actions, but you are responsible for your own infrastructure costs.


https://docs.github.com/en/actions/concepts/runners

---

## Limitations of GitHub Hosted Runners


 1. **Job Execution Time**: GitHub Hosted Runners have a maximum execution time limit of 6 hours per job.
 If a job exceeds this limit, it will be automatically terminated.
 2. **Workflow Run Time**: Each workflow runs is limited to 35 days. If a workflow run exceeds this limit, it will be automatically cancelled.
 This period includes execution duration, and time spent on waiting and approval.
 3. **API requests**: You can execute up to 1000 API requests per hour for a repository. If you exceed this limit, you will receive a 403 Forbidden response until the limit resets. 
 4. **Concurrent Jobs**: The number of concurrent jobs you can run depends on your GitHub plan. 
 Free Plan: 20 concurrent jobs, Pro Plan: 60 concurrent jobs, Team Plan: 180 concurrent jobs, Enterprise Plan: 180 concurrent jobs.

 ## Limitations of Self-Hosted Runners


 1. **Job Execution Time**: Each job in a workflow can run for up to 5 days of execution time on a self-hosted runner. If a job exceeds this limit, it will be automatically terminated.
 2. **Workflow Run Time**: Each workflow run is limited to 35 days. If a workflow run exceeds this limit, it will be automatically cancelled.
 This period includes execution duration, and time spent on waiting and approval.
 3. **API requests**: You can execute up to 1000 API requests per hour for a repository. If you exceed this limit, you will receive a 403 Forbidden response until the limit resets.
 4. **Concurrent Jobs**: The number of concurrent jobs you can run on self-hosted runners depends on the number of runners you have set up and their capacity.
 5. **Job Matrix**: No more than 500 workflow run can be queued in a 10 second interval  for a repository. If you exceed this limit, you will receive a 403 Forbidden response until the limit resets.
 6. **Registring self-hosted runners**: You can register up to 10000 self-hosted runners per repository, organization, or enterprise. 
 If you exceed this limit, you will receive an error message when trying to register additional runners.

---