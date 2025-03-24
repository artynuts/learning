# Testing


### Enforcing code coverage
We can enforce pre-commit checks to enforce code coverage with Husky. The following compares Husky with Native Git Hooks.

1. **Portability**: Husky hooks are installed as part of your npm dependencies, so they're shared with all team members. Native Git hooks stay in the local `.git/hooks` directory and aren't committed to the repository.
2. **Easy setup**: Husky provides a simpler configuration interface through package.json or its own config files, while native hooks require writing shell scripts manually.
3. **Node.js integration**: Since your project is a Node.js/Next.js application, Husky integrates seamlessly with npm scripts, making it easier to run Jest and your coverage checks.
4. **Cross-platform compatibility**: Husky works consistently across Windows, macOS, and Linux, while native Git hooks may face platform-specific issues, especially on Windows.
5. **Maintainability**: When you want to update or modify hooks, Husky's centralized configuration is easier to manage than editing shell scripts in the `.git/hooks` directory.
6. **Developer experience**: Husky includes helpful features like error reporting and compatible with other tools in the JavaScript ecosystem.

Native Git hooks would work, but Husky offers a more developer-friendly experience for JavaScript projects like yours.
