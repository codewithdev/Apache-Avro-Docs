# Contributing to Apache Avro Documentation (exploratory project)

Thank you for your interest in contributing to the Apache Avro Documentation! During Hacktoberfest, we’re especially focused on improving our documentation to help users get the best experience with Apache Avro. Here are some guidelines to help you get started.

> [!NOTE]
> A friendly note about Hacktoberfest Participation
> If you’re participating in Hacktoberfest and want to contribute to this project, ensure to sign up on the Hacktoberfest website. This ensures that your contributions are counted towards the event.


## How to Contribute?
1. Fork this repository by clicking "Fork" button on the top-right to create a copy of it in your profile.
2. Clone your forked repository of this project.
   ```bash
   git clone https://github.com/<your-username>/Apache-Avro-Docs.git
   ```

3. Navigate to the project directory
   ```bash
   cd Apache-Avro-Docs
   ```

4. Install required dependencies
   The documentation is built using Sphinx. You need to have Python installed. 
   ```bash
   pip install -r requirements.txt
   ```
This will install Sphinx and other dependencies.

## What to contribute?
Here are some key areas where we need your help:

### Correcting Typos and Grammar
Improving clarity and readability by fixing typos or rewording confusing phrases.
### Adding Examples
Adding more examples to existing documentation pages to help readers understand the content better.
### Updating Outdated Content
Some pages may contain outdated information. We need help reviewing and updating content to align with the latest version of Apache Avro.
### Improving Structure
Restructuring the content for better flow and navigation.
### Adding New Sections
There may be features or topics that are not well documented. You can help by adding new sections to cover these.

## Helpful resources
We use Sphinx to build the documentation of this project, which means all the content is in reStructuredText (.rst) format. If you’re new to reStructuredText, you can find a quickstart guide here.

### Previewing Your Changes
To preview your changes locally:
1. Build the docs
   ```bash
   make html
   ```
2. Open the Docs in Your Browser
   After building, open the HTML files in the `_build/html` directory to see your changes.


### Making a Pull Request

1. Create a branch
2. Make changes and push the commits
3. Push to your forked repository
4. Raise a Pull request

## Pull Request Guidelines

- Pull Request Size: Please make pull requests focused and avoid bundling multiple unrelated changes.
- Style: Ensure that the writing style is clear, concise, and consistent with the rest of the documentation.
- Code Blocks: Use code blocks where necessary, and make sure to specify the language for syntax highlighting.
- Review: Please be patient while your pull request is being reviewed. We may request changes or provide feedback.

>[!NOTE]
> - Be patient while your PR is being reviewed. Once you have successfully submitted the PR, we will review, and if the changes looks good, will mark your PR as “hacktoberfest-accepted”.
> - PRs may get "rejected" or "closed", if they contain any suspicious content, malaware, or spam and will be counted as invalid contributions.




