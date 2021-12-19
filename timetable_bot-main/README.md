# timetable_bot
Using 'Bot father' and the database, we write a bot with a schedule.
1. Registered the bot in telegram (sent the necessary commands to the Bot father and entered the necessary data).
2.To the file main.py importing libraries to create the back-end part of the bot.
3.Copy the tocken to control the bot.
4. Create a bot object to which we will refer.
5.Creating decorators responding to commands ('/week', '/mtuci', '/help')
6.Create decorators responding to messages (понедельник, вторник, среда, четверг, пятница, расписание на текущую неделю, расписание на следующую неделю)
7. Creating a database
8. Connect to it
9.Creating schemes 'subject', 'timetable', 'teacher'
10.We create a table, fill it in, and also make a connection between the tables
11.Modernizing the application (adding a cursor to access the database, creating a decorator)
12. When entering an unknown command or a message unknown to the bot, the bot sends a message – "Извините, я Вас не понял."
