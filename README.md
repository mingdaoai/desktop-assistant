# Anthropic AI as a Virtual Assistant

Do you spend hours researching the best places to eat and visit when you travel?

With the latest release of Anthropic AI, you can now have a virtual assistant handle all the work for you.

1. Visit [Anthropic](https://console.anthropic.com/dashboard) to create an Anthropic API key.

2. Save the API key in the file located at ~/.mingdaoai/anthropic.key.

3. Install Docker from [Docker](https://www.docker.com/products/docker-desktop) and run the Docker framework.

4. Execute the following command in your terminal's bash shell. Replace `<YOUR_API_KEY>` with the API key you created in step 1.

```bash
git clone https://github.com/mingdaoai/desktop-assistant
cd desktop-assistant
python start_desktop.py
```

5. Launch your web browser and navigate to [http://localhost:8080](http://localhost:8080). You will be greeted by a virtual desktop, accompanied by a chat interface on the left side.

6. Try using this prompt: "I'm at the Washington Monument. Find the most affordable restaurant nearby and guide me on how to get there."