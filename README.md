# Anthropic AI Driving a Computer

When you travel, do you waste hours researching the best place to eat and visit?

With the latest release of Anthropic AI, you can now have a virtual assistant to do all the work for you.

1. Create an Anthropic API key by signing up at [Anthropic](https://console.anthropic.com/dashboard).

2. Save the API key in ~/.mingdaoai/anthropic.key

3. Install Docker from [Docker](https://www.docker.com/products/docker-desktop) and run the docker framework.

4. Run the following command in the bash shell in your terminal. Replace `<YOUR_API_KEY>` with the API key you created in step 1.:

```bash
git clone https://github.com/mingdaoai/anthropic-desktop
cd anthropic-desktop
python start_desktop.py
```

5. Open your browser and go to [http://localhost:8080](http://localhost:8080). You will see a virtual desktop, with a chat dialog to its left.

6. Try this prompt:

I'm at washington monument.  find the cheapest restaurant around here, and show me how to navigate to it.