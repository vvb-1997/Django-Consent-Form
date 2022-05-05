from typing_extensions import Required
from django.db import models
from django import forms

from localflavor.us.models import USStateField, USZipCodeField
from phonenumber_field.modelfields import PhoneNumberField


class NjSchool(models.Model):
    school_name = models.CharField(max_length=255)

    def __str__(self):
        return self.school_name

    class Meta:
        #ordering = ['school_county']
        db_table = "nj_school_name"


class NjSchoolCounty(models.Model):
    school_county = models.CharField(max_length=255)

    def __str__(self):
        return self.school_county

    class Meta:
        db_table = "nj_school_county"


class NjSchoolDistrict(models.Model):
    school_district = models.CharField(max_length=255)

    def __str__(self):
        return self.school_district

    class Meta:
        db_table = "nj_school_district"


class NjWorkLocation(models.Model):
    work_location = models.CharField(max_length=255)

    def __str__(self):
        return self.work_location

    class Meta:
        db_table = "nj_work_location"


class NjConsentData(models.Model):

    CONSENTER_TYPE = (
        ('student', 'student'),
        ('staff', 'staff'),
    )

    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('NonBinary', 'NonBinary'),
        ('Prefer not to answer', 'Prefer not to answer'),
    )
    RACE = (
        ('American Indian/Alaskan Native', 'American Indian/Alaskan Native'),
        ('Asian', 'Asian'),
        ('Black or African American', 'Black or African American'),
        ('Hawaiian Native or Other Pacific Islander', 'Hawaiian Native or Other Pacific Islander'),
        ('White', 'White'),
        ('Not Stated', 'Not Stated'),
    )
    HISPANIC_CHOICE = (
        ('Yes', 'Yes'),
        ('No', 'No'),
        ('Unknown', 'Unknown'),
    )

    first_name = models.CharField('First Name', max_length=130)
    last_name = models.CharField('Last Name', max_length=130)
    gender = models.CharField(max_length=20, choices=GENDER, default=GENDER[0][0])

    school_name = models.ForeignKey(NjSchool, on_delete=models.CASCADE)
    school_county = models.ForeignKey(NjSchoolCounty, on_delete=models.CASCADE)
    school_district = models.ForeignKey(NjSchoolDistrict, on_delete=models.CASCADE)

    consenter_type = models.CharField(max_length=20, choices=CONSENTER_TYPE)
    test_taker_dob = models.DateField()
    address1 = models.CharField("Home Address (Not a PO Box)", max_length=1024)
    address2 = models.CharField("Address line 2", max_length=1024, blank=True)
    zip_code = USZipCodeField("ZIP / Postal code", max_length=12)
    city = models.CharField("City", max_length=1024)
    state = USStateField("State")
    race = models.CharField(max_length=50, choices=RACE, default=RACE[0][0])
    ethnicity = models.CharField('Hispanic/Latino', max_length=20, choices=HISPANIC_CHOICE,
                                 default=HISPANIC_CHOICE[0][0])

    # authorize_checkbox = models.BooleanField(null=False)

    phone_no = PhoneNumberField("Phone")
    email = models.EmailField("Email")

    signature_name = models.CharField(max_length=260)
    date = models.DateField()

class Consent(models.Model):
    OFFICE_LOCATIONS = (
        ('Atlanta, GA', 'Atlanta, GA'),
        ('Boston, MA', 'Boston, MA'),
        ('Chicago, IL', 'Chicago, IL'),
        ('Dallas, TX', 'Dallas, TX'),
        ('Denver, CO', 'Denver, CO'),
        ('Farmington, CT', 'Farmington, CT'),
        ('Houston, TX', 'Houston, TX'),
        ('Los Angeles, CA', 'Los Angeles, CA'),
        ('Miami, FL', 'Miami, FL'),
        ('New York, NY', 'New York, NY'),
        ('Philadelphia, PA', 'Philadelphia, PA'),
        ('San Francisco, CA', 'San Francisco, CA'),
    )
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('NonBinary', 'NonBinary'),
        ('Prefer not to answer', 'Prefer not to answer'),
    )
    RACE = (
        ('American Indian/Alaskan Native', 'American Indian/Alaskan Native'),
        ('Asian', 'Asian'),
        ('Black or African American', 'Black or African American'),
        ('Hawaiian Native or Other Pacific Islander', 'Hawaiian Native or Other Pacific Islander'),
        ('White', 'White'),
        ('Not Stated', 'Not Stated'),
    )
    HISPANIC_CHOICE = (
        ('Yes', 'Yes'),
        ('No', 'No'),
        ('Unknown', 'Unknown'),
    )

    work_location = models.ForeignKey(NjWorkLocation, on_delete=models.CASCADE)
    # work_location = models.ForeignKey(OFFICE_LOCATIONS, default=OFFICE_LOCATIONS[0][0])
    first_name = models.CharField('First Name', max_length=130)
    last_name = models.CharField('Last Name', max_length=130)
    birth_date = models.DateField()

    address1 = models.CharField("Home Address (Not a PO Box)", max_length=1024)
    address2 = models.CharField("Address line 2", max_length=1024, blank=True)
    zip_code = USZipCodeField("ZIP / Postal code", max_length=12)
    city = models.CharField("City", max_length=1024)
    state = USStateField("State")

    phone_no = PhoneNumberField("Phone")
    email = models.EmailField("Email")
    gender = models.CharField(max_length=20, choices=GENDER, default=GENDER[0][0])
    race = models.CharField(max_length=50, choices=RACE, default=RACE[0][0])
    hispanic_latino = models.CharField('Hispanic/Latino', max_length=20, choices=HISPANIC_CHOICE,
                                       default=HISPANIC_CHOICE[0][0])

    signature_name = models.CharField(max_length=260)
    date = models.DateField() 

    # def get_absolute_url(self):
    #     return reverse('success-page')