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

---
