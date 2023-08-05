# Generated by Django 3.2.4 on 2022-07-23 08:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Certification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('authority', models.CharField(max_length=30)),
                ('date_issued', models.CharField(max_length=20)),
                ('document_link', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(max_length=100)),
                ('duration', models.CharField(max_length=15)),
                ('level', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('achievements', models.TextField(blank=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Focus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('icon', models.CharField(max_length=20)),
                ('color', models.CharField(default='white', max_length=20)),
                ('description', models.CharField(max_length=500)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProfessionalSkill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('percentage', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('contact_no', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=200)),
                ('image', models.ImageField(help_text='425x425px recommmended', upload_to='profile_pics')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('linkedin_url', models.CharField(max_length=100)),
                ('github_url', models.CharField(max_length=50)),
                ('instagram_url', models.CharField(max_length=150)),
                ('youtube_url', models.CharField(max_length=150)),
                ('about_me', models.CharField(max_length=500)),
                ('cv_link', models.CharField(blank=True, max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('code', models.CharField(blank=True, max_length=20)),
                ('description', models.TextField()),
                ('date_started', models.CharField(blank=True, max_length=20)),
                ('date_ended', models.CharField(blank=True, max_length=20)),
                ('main_image', models.ImageField(default='', upload_to='project_images')),
                ('repo_link', models.CharField(blank=True, max_length=50)),
                ('demo_link', models.CharField(blank=True, max_length=50)),
                ('document_link', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('code', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('message', models.CharField(max_length=400)),
                ('image', models.ImageField(default='recommendations/default', upload_to='recommendations')),
                ('summary', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Seminar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('organizer', models.CharField(max_length=30)),
                ('event_date', models.CharField(max_length=20)),
                ('link_proof', models.CharField(blank=True, max_length=200)),
                ('link_icon', models.CharField(blank=True, max_length=20)),
                ('document_link', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TechnicalSkill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('is_top_skill', models.BooleanField(default=True)),
                ('percentage', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
                ('duration', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=200)),
                ('summary', models.TextField(blank=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='ToolsAndTech',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('project', models.ManyToManyField(related_name='toolsandtechs', to='contents.Project')),
            ],
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('value', models.CharField(max_length=200)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='project_images')),
                ('caption', models.CharField(blank=True, max_length=100)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projectimages', to='contents.project')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='project_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='contents.projectcategory'),
        ),
    ]
