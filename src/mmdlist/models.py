from django.db import models


class MMDInfo(models.Model):
    # This field type is a guess.
    Index = models.IntegerField(primary_key=True)

    Title = models.CharField(max_length=100, default='', blank=False, null=False)
    TitleEng = models.CharField(max_length=100, default='', blank=True, null=False)
    Artist = models.CharField(max_length=100, default='', blank=False, null=False)

    Cover = models.CharField(max_length=200, default='', blank=True, null=False)

    Type = models.CharField(max_length=20, default='', blank=True, null=False)

    Player = models.IntegerField(default=1)

    Motion = models.CharField(max_length=100, default='', blank=True, null=False)
    MotionEdited = models.BooleanField(default=0, null=False)

    Facial = models.CharField(max_length=100, default='', blank=True, null=False)
    Lipsync = models.CharField(max_length=100, default='', blank=True, null=False)

    Camera = models.CharField(max_length=100, default='', blank=False, null=False)
    CameraEdited = models.BooleanField(default=0, null=False)

    def as_dict(self):
        return {
            "Index": self.Index,
            "Title": self.Title,
            "TitleEng": self.TitleEng,
            "Artist": self.Artist,
            "Cover": self.Cover,
            "Type": self.Type,
            "Player": self.Player,
            "Motion": self.Motion,
            "MotionEdited": self.MotionEdited,
            "Facial": self.Facial,
            "Lipsync": self.Lipsync,
            "Camera": self.Camera,
            "CameraEdited": self.CameraEdited
        }