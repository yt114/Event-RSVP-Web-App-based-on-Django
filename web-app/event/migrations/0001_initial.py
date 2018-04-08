# Generated by Django 2.0.2 on 2018-02-10 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(blank=True, null=True, verbose_name='后台分值')),
                ('content', models.CharField(blank=True, max_length=64, null=True, verbose_name='文本内容')),
            ],
            options={
                'verbose_name_plural': '问题答案表',
            },
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=16, verbose_name='选项名称')),
                ('value', models.CharField(max_length=16, verbose_name='选项值')),
            ],
            options={
                'verbose_name_plural': '选项表',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='问题标题')),
                ('type', models.IntegerField(choices=[(1, '打分'), (2, '单选'), (3, '建议')], verbose_name='问题类型')),
            ],
            options={
                'verbose_name_plural': '问题表',
            },
        ),
        migrations.CreateModel(
            name='Questionnaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='问卷标题')),
            ],
            options={
                'verbose_name_plural': '问卷表',
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=16, verbose_name='用户名')),
                ('password', models.CharField(max_length=16, verbose_name='密码')),
            ],
            options={
                'verbose_name_plural': '用户信息表',
            },
        ),
        migrations.AddField(
            model_name='question',
            name='questionnaire',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.Questionnaire', verbose_name='所属问卷'),
        ),
        migrations.AddField(
            model_name='option',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.Question', verbose_name='所属问题'),
        ),
        migrations.AddField(
            model_name='answer',
            name='option',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='event.Option', verbose_name='对应选项'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.Question', verbose_name='所属问题'),
        ),
    ]