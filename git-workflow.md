# Git Branching and Pull Request Workflow

> This document explains in detail how to work with **branches**, **sub-branches**, and **pull requests** in a collaborative Git workflow.  
> It applies to all developers contributing to this repository and ensures a consistent, high-quality development process.

---

## 1. Understanding Branches

A **branch** in Git represents an independent line of development. It allows multiple people to work on different tasks without interfering with each other’s code.

When you clone a repository, you start on the **`main`** branch (sometimes named `master`). This branch represents the stable version of the code — the one that’s ready for deployment or release.

### Why use branches?
- To **isolate** new features or fixes.
- To **experiment** safely without breaking production code.
- To **collaborate** more effectively by merging only stable code.

### Creating and using branches

```bash
# Create a new branch and switch to it
git checkout -b feature/add-login

# Switch between branches
git checkout main

# Push your branch to the remote repository
git push -u origin feature/add-login
```

Branch names should follow a clear naming convention:
- `feature/<name>` → for new features  
- `bugfix/<issue>` → for bug fixes  
- `hotfix/<issue>` → for urgent fixes in production  
- `chore/<task>` → for maintenance or non-feature changes  

**Example:**  
`feature/user-profile-ui` or `bugfix/login-redirect-loop`

---

## 2. Sub-Branches

A **sub-branch** is a branch created from another feature branch (not from `main`).  
They are useful for working on **dependent tasks** or **parallelizing development** among team members.

### Example
Imagine the team is building a new login system:
1. `feature/new-login` – the main feature branch.  
2. `feature/new-login/api-integration` – a sub-branch for backend API work.  
3. `feature/new-login/ui` – a sub-branch for frontend styling.

Each sub-branch can be merged back into the main feature branch before it’s merged into `main`.

---

## 3. Pull Requests (PRs)

A **Pull Request (PR)** is a formal request to merge changes from one branch into another (typically into `main` or a parent feature branch).

PRs are essential for:
- **Code review** and discussion before merging.  
- **Automated testing** and CI/CD checks.  
- **Tracking** every change introduced into the project.

### Creating a Pull Request

1. Push your branch to the remote repository:
   ```bash
   git push origin feature/add-login
   ```
2. Go to your Git platform (e.g., GitHub, GitLab, Bitbucket).
3. Click **“New Pull Request”**.
4. Choose:
   - **Base branch** → the branch you want to merge *into* (often `main`).
   - **Compare branch** → the branch you worked on.
5. Add:
   - A **descriptive title** (“Add login functionality”)
   - A **clear summary** (“Implements backend OAuth and login UI”)
6. Assign **reviewers** and add **labels** if needed.

---

## 4. Handling Pull Requests

### 4.1. From the Developer’s Side (Author)

The author of a PR should:
- Ensure the branch is **up-to-date** with the base branch:
  ```bash
  git fetch origin
  git merge origin/main
  ```
- Confirm that:
  - All **tests pass** locally.  
  - Code follows **style and linting** rules.  
  - No **sensitive information** (e.g., credentials) is committed.

#### Writing a Good Pull Request Description
A thorough PR description should include:
- **Purpose** – Why this PR exists.  
- **Changes introduced** – Summary of what’s been modified.  
- **Testing** – How the new code was tested.  
- **Impact/Risks** – If it affects other areas of the codebase.

**Example template:**
```markdown
### Summary
Implements user login using JWT authentication.

### Changes
- Added `/login` and `/logout` endpoints
- Refactored user service to handle tokens
- Updated UI to include authentication flow

### Testing
- Unit tests for login/logout
- Manual test in local environment

### Notes
Depends on `auth-service` API being deployed.
```

After review:
- Address feedback from reviewers.
- Commit changes and push updates (the PR updates automatically).
- Once approved, click **Merge** (or request a maintainer to do it).

---

### 4.2. From the Reviewer’s Side (Maintainer)

Reviewers are responsible for maintaining project quality and consistency.

They should:
- Carefully review **code logic**, **security**, and **performance**.
- Check for **readable and maintainable code**.
- Enforce naming and formatting conventions.
- Confirm that all **tests and CI pipelines** pass.
- Leave **constructive feedback** without blocking progress unnecessarily.

If the PR is ready:
- Approve and **merge** using the appropriate method:
  - **Squash merge**: combines all commits into one clean commit.
  - **Rebase and merge**: keeps history linear.
  - **Regular merge**: preserves the full commit history.

If additional changes are required:
- Use **comments or requested changes** to notify the author.
- Avoid merging until all checks are resolved.

---

## 5. Best Practices

- Keep PRs **small and focused** (one purpose per PR).  
- Always **sync with the main branch** before merging.  
- Use **draft PRs** for ongoing work.  
- Delete merged branches to keep the repository clean:
  ```bash
  git branch -d feature/add-login
  git push origin --delete feature/add-login
  ```
- Protect your `main` branch with **branch protection rules** (require PR review and CI pass before merge).

---

## 6. Example Workflow Summary

```bash
# 1. Create a feature branch
git checkout -b feature/add-dashboard

# 2. Work on your code and commit changes
git add .
git commit -m "Add dashboard page"

# 3. Push your branch to remote
git push origin feature/add-dashboard

# 4. Open a pull request to 'main' on GitHub

# 5. Request review and respond to feedback

# 6. Merge once approved

# 7. Delete the branch locally and remotely
git branch -d feature/add-dashboard
git push origin --delete feature/add-dashboard
```

---

## 7. Conclusion

By using **branches** and **pull requests** effectively, your team can maintain a clean, stable codebase, encourage collaboration, and ensure all changes are well-reviewed before reaching production.  
This workflow reduces the risk of conflicts, improves productivity, and builds shared code ownership among developers.
