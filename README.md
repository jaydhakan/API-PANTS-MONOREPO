# API-PANTS-MONOREPO

This is my first project where I tested pants monorepo structure in an API project.

All the mentioned endpoints in PANTS-API.postman_collection.json are working and examples
are written there please go through it.

to run the app create an .env file, please check example.env for reference.

python3 app.py to run the whole FastAPI app with platform and auth both included.

Description of some additional features::

1) added a privilege field while registering a user.
   with a simple function mention in jwt/src/helpers.py you can check a persons
   privilege. example: to get all users you must be logged in as a SUPER_ADMIN.

2) added pants mono-repo infrastructure:

   to use it you need just need to launch this two codes on your terminal:
   (make sure you will need to copy .env to anywhere you want to run pex)

3) to convert whole FastAPI app to one pex file
   terminal command: pants package app

   AND

   ./root_to_pex_file/main.pex (./dist/apps/main.pex) to run pex file from terminal

   ~ pants takes care of everything you just need the same python version to run
   pex file which is 3.12 or greater in our case.

   ~ there are many mare things that can be done with pants like running all test
   cases at once it can create docker image for us can test all the
   run cases in one go, format whole code, etc
