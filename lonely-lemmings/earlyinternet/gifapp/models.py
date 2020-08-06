from django.db import models
import django.contrib.auth.models as md


class User(md.User):
    """data entry model for an app user"""
    profile_picture = models.ImageField(upload_to='profile/')

    def __repr__(self) -> str:
        """returns the username of the user"""
        cls = self.__class__.__name__
        return f"{cls} username={self.username!r}"


class Project(models.Model):
    """data entry model for a project that an user can do, can either be a gif or still image project"""
    name = models.CharField(max_length=50)
    user_id = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    is_gif = models.BooleanField(null=False, default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    preview_version = models.ImageField(upload_to="images/")
    upload_version = models.ImageField(upload_to="images/")

    def __repr__(self) -> str:
        """returns the project name and the owner id that it belongs to"""
        cls = self.__class__.__name__
        return f"{cls} name={self.name!r} owner_id={self.user_id!r}"


class Image(models.Model):
    """data entry model for an image that can be inside a project"""
    project_id = models.ForeignKey(Project, null=False, on_delete=models.CASCADE)
    image_name = models.CharField(max_length=50)
    image_data = models.ImageField(upload_to="images/")
    date_created = models.DateTimeField(auto_now_add=True)
    date_last_modified = models.DateTimeField(auto_now=True)
    animation_position = models.PositiveIntegerField(null=False, default=0)

    def __repr__(self) -> str:
        """returns the image name and the project id that it belongs to"""
        cls = self.__class__.__name__
        return f"{cls} image_name={self.image_name!r} project_id={self.project_id!r}"


class Comment(models.Model):
    """data entry model for a comment on a project or another comment"""
    content = models.TextField()
    post_id = models.ForeignKey(Project, null=False, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    parent_id = models.ForeignKey('self', null=True, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def __repr__(self) -> str:
        """returns the user id of the author and the date created"""
        cls = self.__class__.__name__
        return f"{cls} user_id={self.user_id!r} date_created={self.date_created!r}"
