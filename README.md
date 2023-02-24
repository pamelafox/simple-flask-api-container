This repository includes a simple Python Flask web site, made for demonstration purposes only.
The project can be developed locally with Docker and can be deployed to Azure Container Apps
using the infrastructure files in `infra`. See below for more details.

### Local development

This project has Dev Container support, so you can open it in Github Codespaces or local VS Code with the Dev Containers extension. 

Steps for running the server: 

1. (Optional) If you're unable to open the devcontainer, [create a Python virtual environment](https://docs.python.org/3/tutorial/venv.html#creating-virtual-environments) and activate that.

2. Install the requirements:

```shell
python3 -m pip install -r requirements.txt
```

3. Run the local server: (or use VS Code "Run" button and select "Run server")

```shell
python3 -m flask --debug run
```

3. Click 'http://127.0.0.1:5000' in the terminal, which should open the website in a new tab.

4. Try the index page, try '/hello?name=yourname', and try a non-existent path (to see 404 error).


### Local development with Docker

You can also run this app with Docker, thanks to the `Dockerfile`.
You need to either have Docker Desktop installed or have this open in Github Codespaces for these commands to work.

1. Build the image:

```
docker build --tag flask-app .
```

2. Run the image:

```
docker run --publish 5000:5000 flask-app
```

### Deployment

This repo is set up for deployment on Azure Container Apps (w/PostGreSQL server) using the configuration files in the `infra` folder.

Steps for deployment:

1. Sign up for a [free Azure account](https://azure.microsoft.com/free/)
2. Install the [Azure Dev CLI](https://learn.microsoft.com/azure/developer/azure-developer-cli/install-azd). (If you opened this repository in a devcontainer, that part will be done for you.)
3. Provision and deploy all the resources:

```shell
azd up
```

It will prompt you to login and to provide a name (like "flask-app") and location (like "eastus"). Then it will provision the resources in your account and deploy the latest code. If you get an error with deployment, changing the location (like to "centralus") can help, as there are availability constraints for some of the resources.

4. When `azd` has finished deploying, you'll see an endpoint URI in the command output. Visit that URI, and you should see the front page of the app! 🎉

5. When you've made any changes to the app code, you can just run:

```shell
azd deploy
```

### Costs

Pricing varies per region and usage, so it isn't possible to predict exact costs for your usage.
The majority of the Azure resources used in this infrastructure are on usage-based pricing tiers. 
However, Azure Container Registry has a fixed cost per registry per day.

You can try the [Azure pricing calculator](https://azure.com/e/a0b45ff4228d46baa8ca1dbd15d62afa) for the resources:

- Azure Container App: Consumption tier with 0.5 CPU, 1GiB memory/storage. Pricing is based on resource allocation, and each month allows for a certain amount of free usage. [Pricing](https://azure.microsoft.com/pricing/details/container-apps/)
- Azure Container Registry: Basic tier. [Pricing](https://azure.microsoft.com/pricing/details/container-registry/)
- Key Vault: Standard tier. Costs are per transaction, a few transactions are used on each deploy. [Pricing](https://azure.microsoft.com/pricing/details/key-vault/)
- Log analytics: Pay-as-you-go tier. Costs based on data ingested. [Pricing](https://azure.microsoft.com/pricing/details/monitor/)

⚠️ To avoid unnecessary costs, remember to take down your app if it's no longer in use, 
either by deleting the resource group in the Portal or running `azd down`.


## Getting help

If you're working with this project and running into issues, please post in **Discussions**.
