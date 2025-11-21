from flask import Blueprint, request, render_template

from app.utils.image_handler import process_image
from app.utils.celebrity_detector import CelebrityDetector
from app.utils.qa_engine import QAEngine

import base64

main = Blueprint("main", __name__)

celebrity_detector = CelebrityDetector()
qa_engine = QAEngine()

@main.route("/", methods=["GET", "POST"])
def index():
    celebrity_info =""
    result_img_data = ""
    user_question = ""
    answer = ""

    if request.method == "POST":
        if "image" in request.files:
            image_file = request.files["image"]

            if image_file:
               img_bytes, face_location = process_image(image_file)

               celebrity_info, celebrity_name = celebrity_detector.identify_celebrity(img_bytes)

               if face_location is not None:
                result_img_data = base64.b64encode(img_bytes).decode("utf-8")
               else:
                celebrity_info = "No face detected in the image. Please try again with a different image."
            
        elif "question" in request.form:
            user_question = request.form["question"]
            celebrity_name = request.form["celebrity_name"]
            celebrity_info = request.form["celebrity_info"]
            result_img_data = request.form["result_img_data"]

            answer = qa_engine.ask_about_celebrity(celebrity_name, user_question)

    return render_template("index.html", celebrity_info=celebrity_info, result_img_data=result_img_data, user_question=user_question, answer=answer)

               
                
            

            


             
