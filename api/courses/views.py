from flask_restx import Namespace, Resource


courses_namespace = Namespace('courses', description='name space for authentication')

@courses_namespace.route('/')
class Course(Resource):
    def get(self):
        return{"message": "Hello order nice to meet you"}



# @courses_namespace.route('/courses')
# class Course(Resource):

#     def get(self):

#         """"
#             Get all courses
#         """
#         pass



#     def post(self):

#         """"
#             register all courses
#         """
#         pass


# @courses_namespace.route('/courses/<int:courses_id>')
# class GetUpdateDelete(Resource):

#     def get(self, courses_id):
#         """"
#             Retrieving a courses by id
#         """
#         pass

#     def put(self, courses_id):
#         """"
#             registered courses by id
#         """
#         pass

#     def delete(self, courses_id):
#         """"
#             Delete courses by id
#         """
#         pass

# @courses_namespace.route('/user/<int:students_id>/courses/<int:courses_id>')
# class GetSpecificOrderByUser(Resource):

#     def get(self, students_id, courses_id):
#         """"
#                 Get a specific courses
#         """
#         pass

# @courses_namespace.route('/user/<int:studets_id>/courses')
# class StudentCourses(Resource):
#     def get(self):
#         """
#             Get all students courses
#         """

#         pass

# @courses_namespace.route('/route/status/<int:courses_id>')
# class updateCourseStatus(Resource):

#     def patch(self, courses_id):
#         """
#             Update courses status
#         """
#         pass