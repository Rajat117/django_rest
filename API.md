| Method   | URI | Protected | Description |
| --- | --- | --- | --- |
| POST     | [/api/register] |     No       | Register a user |
| POST     | [/api/login]    |     No       | Log-In a user |
| POST     | [/api/home] |     Yes      | Check Auth |
| POST     | [/api/me] |     Yes      | Get Logged-in User's info |
| POST     | [/api/refresh-token] |     Yes      | Refreshes the user's token |
| POST     | [/api/change-password] |     Yes      | Change User's password |
| POST     | [/api/blogs] |     Yes      | Create a blog |
| GET     | [/api/blogs] |     Yes      | Get authenticated user's  blogs |
| GET     | [/api/blogs/{id}] |     Yes      | Get authenticated user's particular blog |
| PUT     | [/api/blogs/{id}] |     Yes      | Update authenticated user's particular blog |
| DELETE     | [/api/blogs/{id}] |     Yes      | Delete authenticated user's particular blog |
| GET     | [/auth/login/google-oauth2] |     Yes      | Login using gmail account |
| GET     | [/api/login/facebook] |     Yes      | Login Using facebook account |
