# Running Selenium Tests in Docker image located on Docker Hub:

`$ docker run gkgosney/selenium_test:latest`

# Dockerfile used in building image
```
FROM python
RUN apt update
RUN apt-get -y install git vim firefox-esr
RUN pip install -U pytest selenium
RUN git clone https://github.com/tpoopo/SeleniumProject.git
ADD geckodriver-v0.24.0-linux64.tar.gz geckodriver
RUN echo "exec_path=/geckodriver/geckodriver" >> SeleniumProject/config.ini
CMD cd SeleniumProject;pytest SeleniumProject.py
```
# Running Selenium Tests locally
1. Install geckodriver and Firefox if required *
2. Edit SeleniumProject/config.ini and set exec_path to local geckodriver location, set headless to False if desired
3. Install requirements `$ pip3 install -r requirements.txt`
3. Run tests `$ pytest SeleniumProject.py` 



### *This was created using Mozilla Firefox 65.5.0 and geckodriver 0.24.0
