# milpa_productividad.py - Calculadora de productividad milpa tecnificada
# Autor: Basado en SPCM Yucatán y datos orgánicos

# Parámetros editables
pocetas_por_ha = 22000  # Pocetas/ha
semillas_maiz_por_poceta = 3
semillas_frijol_por_poceta = 2
semillas_calabaza_por_poceta = 0.5  # 1 cada 2 pocetas
supervivencia = 0.8  # % plantas establecidas
ciclos_por_ano = 3  # Bajo riego tecnificado

# Rendimientos por planta por ciclo (t/planta; ajusta con datos locales)
# Basados en ~50k plantas maíz para 3.5 t/ciclo
rend_maiz_por_planta_ciclo = 0.000066
rend_frijol_por_planta_ciclo = 0.000037
rend_calabaza_por_planta_ciclo = 0.000455  # Para frutos

# Costos iniciales (MXN/ha) - MODELO EQUIPO PROPIO
costo_equipo_retroexcavadora = 1350000  # CAT 420F usada (Nuevo León)
costo_transporte_equipo = 180000  # Nuevo León → Yucatán (flete)
costo_remolque = 50000  # Remolque cama baja 15 ton
costo_excavacion_por_poceta = 22.89  # Diesel + operador + depreciación equipo
costo_excavacion_ha = pocetas_por_ha * costo_excavacion_por_poceta  # ~$503,580/ha
costo_sustrato_ha = 44000
costo_riego_ha = 45000
costo_infraestructura_ha = costo_excavacion_ha + costo_sustrato_ha + costo_riego_ha

# Costos operativos anuales (MXN/ha) - estimados para mantenimiento
costo_semillas_ha = 3000  # Semillas criollas/orgánicas
costo_fertilizante_organico_ha = 8000  # Compost, biofertilizantes
costo_riego_operacion_ha = 5000  # Energía bomba, mantenimiento
costo_mano_obra_ha = 25000  # Siembra, manejo, cosecha (3 ciclos)
costo_operativo_anual_ha = costo_semillas_ha + costo_fertilizante_organico_ha + costo_riego_operacion_ha + costo_mano_obra_ha

# Precios de venta (MXN/t) - precios orgánicos Yucatán 2025
precio_maiz_t = 8000  # Forraje uso interno (costo oportunidad vs compra externa)
precio_frijol_jamapa_t = 35000  # Frijol orgánico comercial
precio_pepita_calabaza_t = 80000  # Semilla calabaza premium orgánica (10% del peso fruto)

# Mejora productividad por año (factor multiplicador)
# Año 1: 100%, Año 2-3: +10% por mejora suelo, Año 4-5: +15% estabilizado
mejora_productividad = [1.0, 1.1, 1.1, 1.15, 1.15]

# Cálculos base
plantas_maiz_ha = pocetas_por_ha * semillas_maiz_por_poceta * supervivencia
plantas_frijol_ha = pocetas_por_ha * semillas_frijol_por_poceta * supervivencia
plantas_calabaza_ha = pocetas_por_ha * semillas_calabaza_por_poceta * supervivencia

rend_maiz_anual_base = plantas_maiz_ha * rend_maiz_por_planta_ciclo * ciclos_por_ano
rend_frijol_anual_base = plantas_frijol_ha * rend_frijol_por_planta_ciclo * ciclos_por_ano
rend_calabaza_frutos_anual_base = plantas_calabaza_ha * rend_calabaza_por_planta_ciclo * ciclos_por_ano
rend_pepita_anual_base = rend_calabaza_frutos_anual_base * 0.10  # 10% fruto es semilla

# Área del proyecto
ha_lote = 20

# Salida básica
print("=== PRODUCTIVIDAD MILPA TECNIFICADA - TERRA MAYA ORGÁNICA ===")
print(f"\nCONFIGURACIÓN BASE:")
print(f"  Área: {ha_lote} ha")
print(f"  Densidad: {pocetas_por_ha:,} pocetas/ha")
print(f"  Plantas/ha: Maíz {plantas_maiz_ha:,.0f}, Frijol {plantas_frijol_ha:,.0f}, Calabaza {plantas_calabaza_ha:,.0f}")
print(f"\nRENDIMIENTOS AÑO 1 (t/ha):")
print(f"  Maíz grano: {rend_maiz_anual_base:.1f} t/ha")
print(f"  Frijol Jamapa: {rend_frijol_anual_base:.1f} t/ha")
print(f"  Pepita calabaza: {rend_pepita_anual_base:.2f} t/ha")

# PROYECCIÓN 5 AÑOS
print("\n" + "="*80)
print("PROYECCIÓN FINANCIERA 5 AÑOS - LOTE 20 HA")
print("="*80)

# Inversión inicial
inversion_equipo = costo_equipo_retroexcavadora + costo_transporte_equipo + costo_remolque
inversion_infraestructura = costo_infraestructura_ha * ha_lote

# Costos adicionales de inversión inicial
costo_pozo_bomba_total = 100000 * ha_lote  # $100k/ha infraestructura hídrica
costo_semillas_inicial = 24000 * ha_lote  # $24k/ha semillas certificadas
costo_operacion_ciclo1 = 109626 * ha_lote  # $109.6k/ha operación primer ciclo
costo_certificacion = 6000 * ha_lote  # $6k/ha certificación orgánica
contingencias = (inversion_equipo + inversion_infraestructura + costo_pozo_bomba_total + costo_semillas_inicial + costo_operacion_ciclo1 + costo_certificacion) * 0.05

inversion_inicial = inversion_equipo + inversion_infraestructura + costo_pozo_bomba_total + costo_semillas_inicial + costo_operacion_ciclo1 + costo_certificacion + contingencias

print(f"\nINVERSIÓN INICIAL: ${inversion_inicial:,.0f} MXN")
print(f"  Equipo (retroexcavadora + transp. + remolque): ${inversion_equipo:,.0f}")
print(f"  Infraestructura hídrica (pozo + bomba): ${costo_pozo_bomba_total:,.0f}")
print(f"  Semillas certificadas: ${costo_semillas_inicial:,.0f}")
print(f"  Operación primer ciclo: ${costo_operacion_ciclo1:,.0f}")
print(f"  Certificación orgánica: ${costo_certificacion:,.0f}")
print(f"  Contingencias (5%): ${contingencias:,.0f}")
print(f"  Excavación pocetas (equipo propio): ${costo_excavacion_ha * ha_lote:,.0f}")
print(f"  Sustrato orgánico: ${costo_sustrato_ha * ha_lote:,.0f}")
print(f"  Sistema riego: ${costo_riego_ha * ha_lote:,.0f}")

# PUNTO DE EQUILIBRIO - EQUIPO PROPIO
print(f"\n{'='*80}")
print("ANÁLISIS PUNTO DE EQUILIBRIO - EQUIPO PROPIO VS CONTRATADO")
print(f"{'='*80}")
costo_contratado_por_poceta = 35.25  # Costo mercado excavación contratada
ahorro_por_poceta = costo_contratado_por_poceta - costo_excavacion_por_poceta
pocetas_equilibrio = inversion_equipo / ahorro_por_poceta
ha_equilibrio = pocetas_equilibrio / pocetas_por_ha

print(f"\nCosto excavación contratada:    ${costo_contratado_por_poceta:.2f}/poceta")
print(f"Costo excavación equipo propio:  ${costo_excavacion_por_poceta:.2f}/poceta")
print(f"Ahorro por poceta:               ${ahorro_por_poceta:.2f}/poceta")
print(f"\nInversión en equipo:             ${inversion_equipo:,.0f} MXN")
print(f"Pocetas para equilibrio:         {pocetas_equilibrio:,.0f} pocetas")
print(f"Hectáreas para equilibrio:       {ha_equilibrio:.1f} ha")
print(f"\nProyecto actual:                 {ha_lote:.0f} ha ({ha_lote/ha_equilibrio:.1f}x sobre equilibrio)")
ahorro_total_vs_contratado = (costo_contratado_por_poceta * pocetas_por_ha * ha_lote) - (costo_excavacion_por_poceta * pocetas_por_ha * ha_lote + inversion_equipo)
print(f"Ahorro neto vs contratado:       ${ahorro_total_vs_contratado:,.0f} MXN")
print(f"{'='*80}\n")

# Variables acumuladas
ingresos_acumulados = 0
costos_acumulados = inversion_inicial
ganancia_acumulada = -inversion_inicial

print(f"\n{'Año':<6} {'Maíz (t)':<12} {'Frijol (t)':<12} {'Pepita (t)':<12} {'Ingresos':<16} {'Costos Op.':<16} {'Ganancia':<16} {'ROI Acum.':<12}")
print("-" * 120)

for ano in range(1, 6):
    # Productividad con mejora por año
    factor = mejora_productividad[ano - 1]
    maiz_ano = rend_maiz_anual_base * factor * ha_lote
    frijol_ano = rend_frijol_anual_base * factor * ha_lote
    pepita_ano = rend_pepita_anual_base * factor * ha_lote
    
    # Ingresos por producto
    ingreso_maiz = maiz_ano * precio_maiz_t
    ingreso_frijol = frijol_ano * precio_frijol_jamapa_t
    ingreso_pepita = pepita_ano * precio_pepita_calabaza_t
    ingresos_totales = ingreso_maiz + ingreso_frijol + ingreso_pepita
    
    # Costos operativos
    costos_operativos = costo_operativo_anual_ha * ha_lote
    
    # Ganancia neta del año
    ganancia_neta = ingresos_totales - costos_operativos
    
    # Acumulados
    ingresos_acumulados += ingresos_totales
    costos_acumulados += costos_operativos
    ganancia_acumulada += ganancia_neta
    
    # ROI acumulado
    roi_acumulado = (ganancia_acumulada / inversion_inicial) * 100
    
    print(f"{ano:<6} {maiz_ano:<12.1f} {frijol_ano:<12.1f} {pepita_ano:<12.2f} ${ingresos_totales:>14,.0f} ${costos_operativos:>14,.0f} ${ganancia_neta:>14,.0f} {roi_acumulado:>10.1f}%")

# Resumen final
print("\n" + "="*80)
print("RESUMEN 5 AÑOS")
print("="*80)
print(f"Inversión inicial:           ${inversion_inicial:>15,.0f} MXN")
print(f"Ingresos totales acumulados: ${ingresos_acumulados:>15,.0f} MXN")
print(f"Costos operativos acumulados:${costos_acumulados:>15,.0f} MXN")
print(f"Ganancia neta acumulada:     ${ganancia_acumulada:>15,.0f} MXN")
print(f"ROI final (5 años):          {(ganancia_acumulada/inversion_inicial)*100:>15.1f}%")

# Punto de equilibrio
for ano in range(1, 6):
    factor = mejora_productividad[ano - 1]
    ingresos_ano = (rend_maiz_anual_base * factor * ha_lote * precio_maiz_t + 
                    rend_frijol_anual_base * factor * ha_lote * precio_frijol_jamapa_t +
                    rend_pepita_anual_base * factor * ha_lote * precio_pepita_calabaza_t)
    costos_ano = costo_operativo_anual_ha * ha_lote
    ganancia_ano = ingresos_ano - costos_ano
    
    # Calcular ganancia acumulada hasta este año
    ganancia_temp = -inversion_inicial
    for a in range(1, ano + 1):
        f = mejora_productividad[a - 1]
        ing = (rend_maiz_anual_base * f * ha_lote * precio_maiz_t + 
               rend_frijol_anual_base * f * ha_lote * precio_frijol_jamapa_t +
               rend_pepita_anual_base * f * ha_lote * precio_pepita_calabaza_t)
        cost = costo_operativo_anual_ha * ha_lote
        ganancia_temp += (ing - cost)
    
    if ganancia_temp >= 0:
        print(f"\n⭐ PUNTO DE EQUILIBRIO: Año {ano} (ganancia acumulada positiva)")
        break

print("\n" + "="*80)
print("DESGLOSE INGRESOS POR PRODUCTO (Promedio anual 5 años)")
print("="*80)

# Calcular promedios
maiz_promedio = sum([rend_maiz_anual_base * mejora_productividad[i] * ha_lote for i in range(5)]) / 5
frijol_promedio = sum([rend_frijol_anual_base * mejora_productividad[i] * ha_lote for i in range(5)]) / 5
pepita_promedio = sum([rend_pepita_anual_base * mejora_productividad[i] * ha_lote for i in range(5)]) / 5

ingreso_maiz_prom = maiz_promedio * precio_maiz_t
ingreso_frijol_prom = frijol_promedio * precio_frijol_jamapa_t
ingreso_pepita_prom = pepita_promedio * precio_pepita_calabaza_t
ingreso_total_prom = ingreso_maiz_prom + ingreso_frijol_prom + ingreso_pepita_prom

print(f"Maíz (forraje interno):  {maiz_promedio:>8.1f} t/año  →  ${ingreso_maiz_prom:>12,.0f} ({ingreso_maiz_prom/ingreso_total_prom*100:>5.1f}%)")
print(f"Frijol Jamapa (venta):   {frijol_promedio:>8.1f} t/año  →  ${ingreso_frijol_prom:>12,.0f} ({ingreso_frijol_prom/ingreso_total_prom*100:>5.1f}%)")
print(f"Pepita calabaza (venta): {pepita_promedio:>8.2f} t/año  →  ${ingreso_pepita_prom:>12,.0f} ({ingreso_pepita_prom/ingreso_total_prom*100:>5.1f}%)")
print(f"{'TOTAL:':<25} {'':>8}           ${ingreso_total_prom:>12,.0f}")

print("\n" + "="*80)