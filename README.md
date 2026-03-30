1, create my env
    python3 -m venv annavenv
2. activate it:
    source annavenv/bin/activate
3. activate postgrade
    sudo systemctl start postgresql
4. check if its running
    sudo systemctl status postgresql
5. start sql as a super user
    sudo -u postgres psql
3. Activate anna database: 
    psql -U anna -d mybackend


    

# Chatbot server 


## Requirements 

- Sallow user to enter chat room
- Greet the user
- Keep track of users
- Answer user questions
- Recogmnize user has left

## Design

- Use flask_restx to build an API server
- Multiple clients possible --TBD
- Handle each major requirenment with an API endpoint
- Use Test-Driven-Development (TDD) to make sure we have testing
- Use Swagger for initial interaction with server
- Use Swagger, pydoc and good docstrings for documentation
 

# Backend
- Flask REST Api
- PostgreSQL
- Supabase (for postgres)
- Render to Deploy