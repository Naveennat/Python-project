from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi import Request
from fastapi.templating import Jinja2Templates
from fastapi import Form,File
app = FastAPI()
templates = Jinja2Templates(directory="templates")



@app.get("/registerPage", response_class=HTMLResponse)#http://127.0.0.1:8000/registerPage/
def show_service_page(request: Request):
    return templates.TemplateResponse("index.html", context={"request": request})


@app.post("/register") #http://127.0.0.1:8000/register/
def user(first_name: str = Form(), last_name: str = Form(),Email: str = Form(),DOB: str = Form(),mobileNo: int = Form(),Pincode: int = Form()):
    """This service takes details
     from client and return a greeting msg"""
    
    data = open("response.txt","a")
    data.write(first_name +" , "+ last_name+" , "+ Email+" , "+ DOB+" , "+str(mobileNo)+" , "+ str(Pincode))
    data.write("\n")
    data.close()

    return "successfully registered"

    