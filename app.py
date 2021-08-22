
import streamlit as st

from PIL import Image
#Enable garbage collection

#Hide warnings
st.set_option("deprecation.showfileUploaderEncoding", False)

#Set the directory path

banner_path= 'D:/heroku_deployment/yolov4-deepSort/images/od.jpg'
img_path='D:/heroku_deployment/yolov4-deepSort/images/detection1.png'


def about():
	st.write(
		'''
		**YOLO** You Only Look Once.
		YOLOv4 is an object detection algorithm that is an evolution of the YOLOv3 model.

		

        YOLO is an algorithm that uses neural networks to provide real-time 
        object detection. 
        This algorithm is popular because of its speed and accuracy.

        what is new to YOLOv4

        YOLOv4's architecture is composed of CSPDarknet53 as a backbone, spatial pyramid pooling 
        additional module, PANet path-aggregation neck and YOLOv3 head. CSPDarknet53 is a novel 
        backbone that can enhance the learning capability of CNN.

        Why YOLO is so fast

        YOLO is orders of magnitude faster(45 frames per second) than other object detection algorithms.
        The limitation of YOLO algorithm is that it struggles with small objects within the image, for 
        example it might have difficulties in detecting a flock of birds. This is due to the spatial 
        constraints of the algorithm.

        How can you improve my Yolo v4?

            1.YOLOv4 — Ten Tactics to Build a Better Model
            2.Gather More Data.
            3.Image Preprocessing and Augmentation.
            4.Image Input Resolution Size.
            5.When to Use Pretrained Weights.
            6.Choosing a Model Size and Architecture.
            7.Picking Up From a Previous Training Run.
            8.Choosing the Best Model after Training.
            9.Track Your Model Evaluations.

        It can be use fo various puposes...

			1. Real time object detection  
			2. Real time object recognition
			3. detect traffic signals, people, parking meters, and animals
			4. Object Localization
            5. many more.....



View Dev-k web :point_right: http://dev-k-copyright.herokuapp.com/
		''')



 


def main():

        #Set App title
        st.title('YOLOv4- deep sort __Object Tracking')
        #App description
        st.write('''
                **YOLO** You Only Look Once.
                YOLOv4 is an object detection algorithm that is an evolution of the YOLOv3 model.

                YOLO is an algorithm that uses neural networks to provide real-time 
                object detection. 
                This algorithm is popular because of its speed and accuracy.
        '''
        )
        st.write('**For more info:**Code:** [Github repository](https://github.com/koushik1234) **|** **Contact info:** [LinkedIn](https://www.linkedin.com/in/koushikahamed1234/)')
        st.markdown('***')

        activities = ["Home", "About"]
        sidebar_choice = st.sidebar.selectbox("Pick something fun", activities)
        sidebar_image=Image.open(banner_path)
        st.sidebar.image(sidebar_image,use_column_width=True)
        st.sidebar.info('© 2021 Copyright: Dev-k')

        if sidebar_choice=="Home":
                st.write(
		'''
		**YOLO** You Only Look Once.
		YOLOv4 is an object detection algorithm that is an evolution of the YOLOv3 model.

        YOLO is an algorithm that uses neural networks to provide real-time 
        object detection. 
        This algorithm is popular because of its speed and accuracy.

        what is new to YOLOv4

        YOLOv4's architecture is composed of CSPDarknet53 as a backbone, spatial pyramid pooling 
        additional module, PANet path-aggregation neck and YOLOv3 head. CSPDarknet53 is a novel 
        backbone that can enhance the learning capability of CNN.

        It can be use fo various puposes...

			1. Real time object detection  
			2. Real time object recognition
			3. detect traffic signals, people, parking meters, and animals
			4. Object Localization
            5. many more.....



View Dev-k web :point_right: http://dev-k-copyright.herokuapp.com/
		''')
                img=Image.open(img_path)
                st.write('**Tracking objects in an Image**')
                st.image(img,use_column_width=True)
                st.write('**Demo-Deep sort** check out the below vedio.')
                video_file = open('D:/heroku_deployment/yolov4-deepSort/results.mp4', 'rb')
                video_bytes = video_file.read()

                st.video(video_bytes)

                
        elif sidebar_choice == "About":
                about()





if __name__ == "__main__":
    main()