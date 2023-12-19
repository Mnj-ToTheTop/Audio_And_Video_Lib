# Flow of Control

The project starts with a page that gives the user an option to login as a customer or an employee.

1. Customer: On logging in as a customer the user will be prompted to login using user id and password. New users will be encouraged to create their own user id and password. Once logged in successfully the user will be directed to the main page of the application with a greeting. The user will be given three options:
      1. Available Videos: On clicking this option the user will be given a list of the available videos. On clicking a desired video title a new window will open. This window contains three buttons:
          1. Play: To play the video.
          2. Pause and Play: To pause and play video.
          3. Stop: To stop the video.

      2. Available Audios: On clicking this option the user will be given a list of the available audios. On clicking a desired audio title a new window will open. This window contains three buttons:
          1. Play: To play the audio.
          2. Pause and Play: To pause and play audio.
          3. Stop: To stop the audio.

      3. Request Content: This option will direct the user to the Request Page. Here, the user will be allowed to request content they want in the library. They will be prompted to enter the Title of the content and the file type in which they want to have the content in. On clicking on “SUBMIT” their request will be stored in the Requested table of the database.

2. Employee: On choosing to login as an employee, the user will be prompted to login using their employee id and password. On successful logging in the user will have the option to view all the requested content or update the library.
      1. Requested Content: This allows the employee to view all the content that has been requested by the users along with the requester.
      2. Update Library: This option allows the employee to add an audio/video and remove them simultaneously from the requested list. 
