package com.example.datacollecter;

import androidx.room.*;

//Used to achieve desensitization before storage
@Database(entities = {ActivityLog.class}, version = 1, exportSchema = false)
abstract class ActivityDatabase{
}
