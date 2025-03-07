##🔍 Insights y Posibles Análisis a Realizar

1) 1️⃣ Limpieza y Tratamiento de Datos

    Hay valores nulos en Mental_Health_Condition (23.92%) y Physical_Activity (32.58%).

    Ambas variables son significativas que poseean valores nulos ya que significa ausencia de la enfermedad , y ausencua de actividad fisica. 



numeric_vars = ['Age', 'Years_of_Experience', 'Hours_Worked_Per_Week', 'Number_of_Virtual_Meetings']
categorical_vars = ['Gender', 'Job_Role', 'Industry', 'Work_Location', 'Mental_Health_Condition', 
                    'Access_to_Mental_Health_Resources', 'Productivity_Change', 'Region']
ordinal_vars = ['Stress_Level', 'Satisfaction_with_Remote_Work', 'Physical_Activity', 
                'Sleep_Quality', 'Work_Life_Balance_Rating', 'Social_Isolation_Rating', 'Company_Support_for_Remote_Work']


GRAFICOS PARA VER LA DISTRIBUCION

2) MODIFICACION DE VARIABLES, DE CATEGORIAS/ ORDINALES A NUMERICAS