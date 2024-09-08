<h1 align="center">🤖 Machine Learning Project</h1>
<p align="center" id="objetivo">Learning MLOps. 
</p> 

<p align="center">
 <a href="#overview">Overview</a> •
 <a href="#features">Technologies and Tools Used</a> •
 <a href="#started">Getting Started</a> • 
 <a href="#author">Author</a>
</p>

<h4 align="center"> 
	🚧  MLOps Project 🚀 Finished  🚧 
</h4>

### Overview

<div style='margin: 20px' id="overview">
This project demonstrates the setup of a Data Version Control (DVC) system using Google Cloud Storage (GCS) as the remote storage for data versioning. It leverages Docker for containerization, Hydra for configuration management, and Poetry for dependency management.
</div>

### Technologies and Tools Used

<div id="features">

- **Docker**: Used to containerize the application, making it portable and easier to deploy in different environments.
- **GCP (Google Cloud Platform)**: Google Cloud Storage is used to store raw data and manage versioning through DVC.
- **Hydra**: Manages the configuration schema for the project, helping with flexible and hierarchical configuration setups.
- **DVC**: Used for versioning datasets and model files. It helps in tracking changes and managing large files efficiently.
- **Poetry**: Handles dependency management, ensuring all required packages are installed in a virtual environment.

</div>

<div id="started">

### Getting Started

To get started with this project, follow these steps:

1. **Clone the Repository:**

   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```
   
2. **Create environtment:**

   ```bash
   # To install and update dependencies
   make lock-dependencies
   
   # Build the docker container
   # make build
   ```
3. **Update Dataset**
   
   ```bash
   # Updates dataset in GCP and push changes to github repository
   make version-data
   ```

</div>


### Author

---

<!-- <script type="text/javascript" src="https://platform.linkedin.com/badges/js/profile.js" async defer></script> -->

<div align="left" id="author">

<a href="https://github.com/danhenriquex">
  <img src="https://github.com/danhenriquex.png" width="100" height="100" style="border-radius: 50%"/>
</a>

<!-- <div class="LI-profile-badge"  data-version="v1" data-size="medium" data-locale="pt_BR" data-type="vertical" data-theme="dark" data-vanity="danilo-henrique-santana"><a class="LI-simple-link" href='https://br.linkedin.com/in/danilo-henrique-santana?trk=profile-badge'>Danilo Henrique</a></div> -->
</div>

<div style="margin-top: 20px" >
  <a href="https://www.linkedin.com/in/danilo-henrique-480032167/">
    <img  src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"/>
  </a>
</div>

