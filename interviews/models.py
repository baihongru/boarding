from django.db import models
from django.db.models.fields import DecimalField
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Candidate(models.Model):
    class InterviewResultType(models.TextChoices):
        """面试结果类型。"""
        PASS = 'PASS', _('通过')
        UNDETERMINED = 'UNDETERMINED', _('待定')
        DROP = 'DROP', _('放弃')
    
    class AbilityGradeType(models.TextChoices):
        """能力评级类型。"""
        S = 'S', _('S')
        A = 'A', _('A')
        B = 'B', _('B')
        C = 'C', _('C')
    
    class DegreeType(models.TextChoices):
        """候选人学历。"""
        BACHELOR = 'BACHELOR', _('本科')
        MASTER = 'MASTER', _('硕士')
        DOCTOR = 'DOCTOR', _('博士')
    
    class GenderType(models.TextChoices):
        """性别。"""
        MALE = 'MALE', _('男')
        FEMALE = 'FEMALE', _('女')
        OTHER = 'OTHER', _('其他')
    
    # 基本信息
    userid = models.IntegerField(
        unique=True,
        blank=True,
        null=True,
        verbose_name='应聘者ID',
    )

    username = models.CharField(
        max_length=100,
        verbose_name='姓名',
    )

    city = models.CharField(
        max_length=100,
        verbose_name='城市',
    )

    phone = models.CharField(
        max_length=100,
        verbose_name='手机号码',
    )

    email = models.EmailField(
        max_length=100,
        verbose_name='邮箱',
    )

    apply_position = models.CharField(
        max_length=100,
        verbose_name='应聘职位',
    )

    born_address = models.CharField(
        blank=True,
        max_length=100,
        verbose_name='生源地',
    )

    gender = models.CharField(
        max_length=100,
        choices=GenderType.choices,
        verbose_name='性别',
    )

    candidate_remark = models.TextField(
        blank=True,
        max_length=1000,
        verbose_name='候选人信息备注',
    )

    # 学校与学历信息
    bachelor_school = models.CharField(
        blank=True,
        max_length=100,
        verbose_name='本科学校',
    )

    master_school = models.CharField(
        blank=True,
        max_length=100,
        verbose_name='硕士学校',
    )

    doctor_school = models.CharField(
        blank=True,
        max_length=100,
        verbose_name='博士学校',
    )

    major = models.CharField(
        blank=True,
        max_length=100,
        verbose_name='专业',
    )

    degree = models.CharField(
        blank=True,
        max_length=100,
        choices=DegreeType.choices,
        verbose_name='学历',
    )

    # 综合能力测评成绩
    comprehensive_score = DecimalField(
        blank=True,
        null=True,
        max_digits=3,
        decimal_places=1,
        verbose_name='综合能力测评得分',
    )

    # 笔试测评成绩
    paper_score = DecimalField(
        blank=True,
        null=True,
        max_digits=3,
        decimal_places=1,
        verbose_name='笔试得分',
    )

    # 第一轮面试记录
    first_score = models.DecimalField(
        blank=True,
        null=True,
        max_digits=2,
        decimal_places=1,
        verbose_name='一面得分',
    )

    first_score_learning = models.DecimalField(
        blank=True,
        null=True,
        max_digits=2,
        decimal_places=1,
        verbose_name='学习能力得分',
    )

    first_score_professional = models.DecimalField(
        blank=True,
        null=True,
        max_digits=2,
        decimal_places=1,
        verbose_name='专业能力得分',
    )

    first_advantage = models.TextField(
        blank=True,
        max_length=1000,
        verbose_name='优势',
    )

    first_disadvantage = models.TextField(
        blank=True,
        max_length=1000,
        verbose_name='顾虑和不足',
    )

    first_result = models.CharField(
        blank=True,
        max_length=100,
        choices=InterviewResultType.choices,
        verbose_name='一面结果',
    )

    first_recommend_position = models.CharField(
        blank=True,
        max_length=100,
        verbose_name='推荐部门',
    )

    first_interviewer = models.CharField(
        blank=True,
        max_length=100,
        verbose_name='面试官',
    )

    first_remark = models.TextField(
        blank=True,
        max_length=1000,
        verbose_name='一面备注',
    )

    # 第二轮面试记录
    second_score = models.DecimalField(
        blank=True,
        null=True,
        max_digits=2,
        decimal_places=1,
        verbose_name='二面得分',
    )

    second_score_learning = models.DecimalField(
        blank=True,
        null=True,
        max_digits=2,
        decimal_places=1,
        verbose_name='学习能力得分',
    )

    second_score_professional = models.DecimalField(
        blank=True,
        null=True,
        max_digits=2,
        decimal_places=1,
        verbose_name='专业能力得分',
    )

    second_score_excellent = models.DecimalField(
        blank=True,
        null=True,
        max_digits=2,
        decimal_places=1,
        verbose_name='追求卓越得分',
    )

    second_score_communication = models.DecimalField(
        blank=True,
        null=True,
        max_digits=2,
        decimal_places=1,
        verbose_name='沟通能力得分',
    )

    second_score_anti_pressure = models.DecimalField(
        blank=True,
        null=True,
        max_digits=2,
        decimal_places=1,
        verbose_name='抗压能力得分',
    )

    second_advantage = models.TextField(
        blank=True,
        max_length=1000,
        verbose_name='优势',
    )

    second_disadvantage = models.TextField(
        blank=True,
        max_length=1000,
        verbose_name='顾虑和不足',
    )

    second_result = models.CharField(
        blank=True,
        max_length=100,
        choices=InterviewResultType.choices,
        verbose_name='二面结果',
    )

    second_recommend_position = models.CharField(
        blank=True,
        max_length=100,
        verbose_name='建议方向或推荐部门',
    )

    second_interviewer = models.CharField(
        blank=True,
        max_length=100,
        verbose_name='面试官',
    )

    second_remark = models.TextField(
        blank=True,
        max_length=1000,
        verbose_name='二面备注',
    )

    # 第三轮面试记录
    third_score = models.CharField(
        blank=True,
        max_length=10,
        choices=AbilityGradeType.choices,
        verbose_name='三面评级',
    )

    third_score_responsibility = models.CharField(
        blank=True,
        max_length=10,
        choices=AbilityGradeType.choices,
        verbose_name='责任心评级',
    )

    third_score_communication = models.CharField(
        blank=True,
        max_length=10,
        choices=AbilityGradeType.choices,
        verbose_name='坦诚沟通评级',
    )

    third_score_logic = models.CharField(
        blank=True,
        max_length=10,
        choices=AbilityGradeType.choices,
        verbose_name='逻辑思维评级',
    )

    third_score_potential = models.CharField(
        blank=True,
        max_length=10,
        choices=AbilityGradeType.choices,
        verbose_name='发展潜力评级',
    )

    third_score_stability = models.CharField(
        blank=True,
        max_length=10,
        choices=AbilityGradeType.choices,
        verbose_name='稳定性评级',
    )

    third_advantage = models.TextField(
        blank=True,
        max_length=1000,
        verbose_name='优势',
    )

    third_disadvantage = models.TextField(
        blank=True,
        max_length=1000,
        verbose_name='顾虑和不足',
    )

    third_result = models.CharField(
        blank=True,
        max_length=100,
        choices=InterviewResultType.choices,
        verbose_name='三面结果',
    )

    third_interviewer = models.CharField(
        blank=True,
        max_length=100,
        verbose_name='面试官',
    )

    third_remark = models.TextField(
        blank=True,
        max_length=1000,
        verbose_name='三面备注',
    )

    # 候选人创建人信息
    creator = models.CharField(
        blank=True,
        max_length=100,
        verbose_name='候选人创建人',
    )

    created_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='创建时间',
    )

    modified_date = models.DateTimeField(
        blank=True,
        null=True,
        auto_now=True,
        verbose_name='更新时间',
    )

    last_editor = models.CharField(
        blank=True,
        max_length=100,
        verbose_name='最后编辑者',
    )

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'candidate'
        verbose_name = '应聘者'
        verbose_name_plural = '应聘者'
