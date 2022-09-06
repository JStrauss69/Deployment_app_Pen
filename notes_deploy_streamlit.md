[[build_web_app]]
[[deploy_web_app]]
[[DS]]
[[week_11]]

# Deploying a web app 
## After this encounter
* you should have a minimal setup to be able to deploy your recommender app to `streamlit`platform
	- create a `conda`-env,
	- have access to `streamlit` platform in order to manage your app
* know about some introductory methods of `streamlit`
* you should be apply to apply the workflow for deploying apps to `streamlit`
* you should be able to share your app with third parties via `streamlit` ;)

## on streamlit
* Open source app-framenwork for ML
    - Allows creating simple web apps based on python code
    - Allows creating advanced web apps without investing too much time in the development of the app

* `streamlit` 
    - removes burden of running web apps
    - takes care of infrastructure
    - enables users to focus on the app itself
* characteristics of `streamlit` (in comparison with `heroku`)
    - no need to create any additional files (such as `Profile`) for running app

## run app locally 
### create an environment
    1. create a virtual env (conda) (based on predefined libs)
`conda env create -f stenv.yml`
    2. test env by running 
`streamlit hello`
    3. run app on localhost using
`streamlit run <name_of_app>`

## deploy app to `streamlit cloud`, https://streamlit.io/cloud
1. create an account at streamlit 
2. clone a remote repo and push stack 
3. deploy on cloud (linking to correspondent repo on `GitHub`)

## references
1. https://docs.streamlit.io/
2. https://30days.streamlitapp.com/?challenge=Day+6
3. https://discuss.streamlit.io/t/streamlit-components-community-tracker/4634
 

