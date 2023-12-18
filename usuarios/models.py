from django.db import models
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

class UserRegisterManager(models.Manager):
    def create_user(self, **extra_fields):
        user = self.model(**extra_fields)
        user.save(using=self._db)
        return user
    
class UserRegister(models.Model):
    GENDER_CHOICES = (
        ("M", "masculino"),
        ("F", "feminino"),
    )

    STATE_CHOICES = (
        ('AC', 'Acre'),('AL', 'Alagoas'),('AP', 'Amapá'),('AM', 'Amazonas'),('BA', 'Bahia'),('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),('ES', 'Espirito Santo'),('GO', 'Goiás'),('MA', 'Maranhão'),('MS', 'Mato Grosso do Sul'),
        ('MT', 'Mato Grosso'),('MG', 'Minas Gerais'),('PA', 'Pará'),('PB', 'Paraíba'),('PR', 'Paraná'),('PE', 'Pernambuco'),('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),('RN', 'Rio Grande do Norte'),('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),('RR', 'Roraima'),('SC', 'Santa Catarina'),('SP', 'São Paulo'),('SE', 'Sergipe'),('TO', 'Tocantins')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id_user = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50, verbose_name = "Primeiro Nome")
    last_name = models.CharField(max_length=50, blank=True, verbose_name = "Último nome")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=None, verbose_name = "sexo")
    birth_date = models.DateField(verbose_name="Data de Nascimento")
    cpf = models.CharField(max_length=11, default='11111111111', verbose_name="cpf")
    address = models.CharField(max_length=255, verbose_name="Rua/Avenida")
    city = models.CharField(max_length=255, verbose_name = "Cidade")
    state = models.CharField(max_length=2, choices=STATE_CHOICES, default=None, verbose_name="Estado")
    zip_code = models.CharField(max_length=10, verbose_name="cep")
    email = models.EmailField(max_length=50, unique=True, verbose_name = "E-mail")
    phone = models.CharField(max_length=255, verbose_name="Telefone")
    password = models.CharField(max_length=20, verbose_name = "Senha")
    confirm_password = models.CharField(max_length=20, verbose_name = "Confirmar Senha", default=None)
    created_at = models.DateTimeField(default = timezone.now)

    objects = UserRegisterManager()


    
    