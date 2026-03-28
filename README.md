### GitHub Actions Information

## Variable and Secret in GitHub Actions workflow

# Using variables in GH Actions
---
**variables for single workflow**:
Define it using the 'env' key in the workflow file. 
The scope of custome variable set by this method is limited to the element in which it is defined.
You can define variables that are scoped for:
- The entire workflow, by using 'env' at the top level of the workflow file
- The content of a job within a workflow
- A spacific step within a job

---
