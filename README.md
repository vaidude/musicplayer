
 Emotion-Based Music Recommendation

This project is a web application that recommends music based on the user's detected emotion. 
Using machine learning or mood-detection APIs, the system identifies the mood of the user and suggests a curated list of songs from Spotify based on that emotion. 
The music recommendations are displayed in a visually appealing interface, utilizing Tailwind CSS for styling.

 Features

- Emotion Detection: Displays the detected emotion from a user input or API.
- Music Recommendations: Based on the detected emotion, the application fetches music recommendations.
- Spotify Integration: Songs are embedded via Spotify if available, with the option to play directly from the page.
- Responsive Design: The web interface is fully responsive, designed to work on all screen sizes (desktop, tablet, mobile).
- Autoplay (if possible): Attempts to autoplay the first song in the recommendation list.

 Technologies Used

- Django: Backend framework for serving the web pages and handling data.
- Tailwind CSS: Utility-first CSS framework for responsive and modern UI.
- HTML & JavaScript: For frontend structure and dynamic interactions.
- Emotion Detection : custom API to detect the user's mood.

 Installation Instructions

 1. Clone the repository

First, clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/emotion-based-music-recommendation.git
```

 2. Set up the virtual environment

Navigate to the project directory and set up a virtual environment:

```bash
cd emotion-based-music-recommendation
python -m venv venv
```

Activate the virtual environment:

- On Windows:
  ```bash
  venv\Scripts\activate
  ```
- On macOS/Linux:
  ```bash
  source venv/bin/activate
  ```

 3. Install dependencies

Install the necessary Python packages using `pip`:

```bash
pip install -r requirements.txt
```

Make sure to have `Django` and any other required packages (such as `requests` or `spotipy`) listed in your `requirements.txt`.

 4. Set up static and media files

To serve static files (like Tailwind CSS) and media files (like images for moods), run the following commands:

```bash
python manage.py collectstatic
```

 5. Configure your API keys

If you are using an Emotion Detection API and the Spotify API, make sure to set your API keys in your Django settings or environment variables:

- Spotify API: Get your API credentials from [Spotify for Developers](https://developer.spotify.com/).
- Emotion Detection API: Set up an account with a mood-detection service (like Affectiva or a custom model) and add your API credentials.

 6. Run the development server

After setting everything up, you can run the Django development server:

```bash
python manage.py runserver
```

 7. Open the application

Open a web browser and visit:

```
http://127.0.0.1:8000/
```

You should see the "Emotion-Based Music Recommendation" application in action.

 Usage

- Emotion Detection: The application automatically detects the user's emotion based on inputs (which could be from an uploaded image or live webcam feed).
- Music Recommendations: Based on the detected mood, songs are fetched from Spotify and displayed. The first song in the list attempts to autoplay, though this may be blocked by browser settings.
- Spotify Integration: Each recommended song has an embedded Spotify player and a link to open the song in Spotify.

 Customizing the Application

- Adding More Emotions: To support additional emotions, you can expand the logic in the backend to handle more moods and fetch corresponding playlists or songs from the Spotify API.
- Enhancing Recommendations: Modify the recommendation logic to include more advanced algorithms or integrate other music sources.

 Contributing

We welcome contributions to this project! If you want to add a new feature, fix a bug, or improve the documentation, feel free to open a pull request. Please make sure to follow these guidelines:

1. Fork the repository and create a new branch.
2. Write tests for any new features or changes.
3. Ensure all existing tests pass.
4. Update the documentation as needed.

 License

This project is licensed under the MIT License

---

 Contact

If you have any questions or feedback, feel free to reach out!

- Author:vaidude






