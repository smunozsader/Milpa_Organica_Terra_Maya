# GUÍA TÉCNICA: Calculadora de Productividad Milpa Tecnificada
**Terra Maya Orgánica - Sistema SPCM Yucatán**

---

## 🎛️ PALANCAS DE CONTROL (Variables Modificables)

### **Top 10 Variables que Controlan los Resultados**

| # | Variable (Línea) | Valor Actual | Rango Válido | Impacto ROI | Descripción |
|---|-----------------|--------------|--------------|-------------|-------------|
| **1** | `precio_frijol_jamapa_t` (37) | $35,000/t | $18,000 - $45,000 | 🔴 **±18%** | Precio venta frijol orgánico certificado |
| **2** | `supervivencia` (9) | 0.8 (80%) | 0.6 - 0.9 | 🔴 **±15%** | % plantas establecidas post-siembra |
| **3** | `rend_frijol_por_planta_ciclo` (14) | 0.000037 t | 0.000030 - 0.000045 | 🔴 **±12%** | Rendimiento frijol por planta/ciclo |
| **4** | `costo_mano_obra_ha` (34) | $25,000/ha | $18,000 - $35,000 | 🟡 **±8%** | Mano obra anual (siembra, manejo, cosecha) |
| **5** | `ciclos_por_ano` (10) | 3 | 1 - 3 | 🟡 **±30%** | Ciclos/año (depende riego; NO modificar a fracciones) |
| **6** | `precio_pepita_calabaza_t` (38) | $80,000/t | $45,000 - $100,000 | 🟡 **±7%** | Precio export pepita orgánica |
| **7** | `precio_maiz_t` (36) | $8,000/t | $6,000 - $10,000 | 🟡 **±4%** | Precio maíz FVH (costo oportunidad compra evitada) |
| **8** | `pocetas_por_ha` (5) | 22,000 | 15,000 - 30,000 | 🟡 **±6%** | Densidad pocetas (afecta plantas y costos excavación) |
| **9** | `rend_maiz_por_planta_ciclo` (13) | 0.000066 t | 0.000050 - 0.000075 | 🟡 **±5%** | Rendimiento maíz por planta/ciclo |
| **10** | `mejora_productividad[4]` (42) | 1.15 | 1.0 - 1.3 | 🟢 **±5%** | Mejora año 5 por biofábricas |
| **11** | `ha_lote` (56) | 20 ha | 5 - 250 | 🟢 **±Escala** | Área total proyecto (análisis escalamiento) |

**🎯 Recomendación de Uso:**
- **Optimización financiera:** Enfocar en variables #1, #6, #7 (**3 PRECIOS: frijol, pepita, maíz**) + #3 (rendimientos)
- **Optimización operativa:** Enfocar en variables #4, #8, #10 (costos y manejo)
- **Análisis de riesgo:** Crear escenarios variando **precios** (#1 frijol ±20%, #6 pepita ±15%, #7 maíz ±10%) y #2 (supervivencia ±10%)
- **Expansión:** Modificar #11 (ha_lote) a 50, 100, 250 para proyectar escalamiento

**⚠️ Variables NO Modificables (Calculadas):**
- Costos de equipo ($3.395M - decisión estratégica tomada)
- Costos infraestructura/ha ($465,500 - basados en análisis técnico)
- Plantas/ha (calculadas de: pocetas × semillas × supervivencia)

---

## 📋 DESCRIPCIÓN GENERAL

La calculadora [`milpa_productividad.py`](milpa_productividad.py) es un modelo financiero y agronómico que proyecta la productividad y rentabilidad de una milpa tecnificada bajo el **Sistema de Producción Continua de Maíz (SPCM)** adaptado a condiciones orgánicas.

**Objetivo principal:** Calcular rendimientos de cultivos, costos de inversión/operación y retorno de inversión (ROI) para un proyecto de 20 hectáreas durante 5 años.

**Basado en:**
- Investigación CICY (Centro de Investigación Científica de Yucatán) sobre SPCM
- Sistema de pocetas con sustrato orgánico en suelos cársticos (litosol)
- Policultivo intercalado: maíz + frijol + calabaza
- Riego tecnificado con fertirrigación (3 ciclos/año)

---

## 🔧 PARÁMETROS CRÍTICOS (Inputs Editables)

### **1. DENSIDAD Y SIEMBRA** (Líneas 5-9)

```python
pocetas_por_ha = 22000  # Pocetas/ha
semillas_maiz_por_poceta = 3
semillas_frijol_por_poceta = 2
semillas_calabaza_por_poceta = 0.5  # 1 cada 2 pocetas
supervivencia = 0.8  # % plantas establecidas
ciclos_por_ano = 3  # Bajo riego tecnificado
```

| Parámetro | Valor Base | Rango Recomendado | Impacto en Cálculos |
|-----------|------------|-------------------|---------------------|
| **`pocetas_por_ha`** | 22,000 | 15,000 - 30,000 | 🔴 **CRÍTICO**: Determina plantas totales/ha y costo excavación |
| **`semillas_maiz_por_poceta`** | 3 | 2 - 4 | 🟡 Alto: Afecta densidad maíz y rendimiento total |
| **`semillas_frijol_por_poceta`** | 2 | 1 - 3 | 🟡 Alto: Afecta mix policultivo |
| **`semillas_calabaza_por_poceta`** | 0.5 | 0.3 - 1.0 | 🟢 Medio: Cultivo secundario |
| **`supervivencia`** | 0.8 (80%) | 0.6 - 0.9 | 🔴 **CRÍTICO**: Reduce plantas efectivas (mortalidad post-siembra) |
| **`ciclos_por_ano`** | 3 | 1 - 3 | 🔴 **CRÍTICO**: Multiplica rendimiento anual (depende de riego) |

**⚠️ Validaciones recomendadas:**
- Si `supervivencia < 0.6` → Problemas en siembra o sustrato
- Si `ciclos_por_ano = 1` → Sistema tradicional sin riego (rendimientos bajan 66%)
- Total semillas/poceta = `maíz + frijol + calabaza` ≈ 5.5 semillas (debe caber en volumen poceta ~50L)

---

### **2. RENDIMIENTOS POR PLANTA** (Líneas 12-15)

```python
rend_maiz_por_planta_ciclo = 0.000066  # t/planta/ciclo
rend_frijol_por_planta_ciclo = 0.000037  # t/planta/ciclo
rend_calabaza_por_planta_ciclo = 0.000455  # t frutos/planta/ciclo
```

| Parámetro | Valor Base | Cálculo Reverso | Impacto |
|-----------|------------|-----------------|---------|
| **`rend_maiz_por_planta_ciclo`** | 0.000066 t | → 3.5 t/ha/ciclo con 52,800 plantas/ha | 🔴 **CRÍTICO**: Determina producción maíz |
| **`rend_frijol_por_planta_ciclo`** | 0.000037 t | → 1.3 t/ha/ciclo con 35,200 plantas/ha | 🔴 **CRÍTICO**: Frijol Jamapa (principal ingreso) |
| **`rend_calabaza_por_planta_ciclo`** | 0.000455 t | → 4.0 t frutos/ha/ciclo con 8,800 plantas/ha | 🟡 Alto: Pepita vale $80k/t |

**Fórmula de validación:**
```
Rendimiento t/ha/ciclo = plantas_ha × rend_por_planta_ciclo
plantas_ha = pocetas_ha × semillas_por_poceta × supervivencia

Ejemplo maíz:
plantas_maiz_ha = 22,000 × 3 × 0.8 = 52,800
rend_maiz_ciclo = 52,800 × 0.000066 = 3.48 t/ha ✓ (meta SPCM: 3.5 t/ha)
```

**⚠️ Límites agronómicos (validar vs SPCM):**
- Maíz: **Max 3.5 t/ha/ciclo** (10.5 t/ha/año × 3 ciclos)
- Frijol: **Max 1.5 t/ha/ciclo** (4.5 t/ha/año × 3 ciclos)
- Calabaza: **Max 5.0 t frutos/ha/ciclo** (15 t/ha/año × 3 ciclos)

---

### **3. COSTOS OPERATIVOS ANUALES** (Líneas 30-35)

```python
costo_semillas_ha = 3000  # Semillas criollas/orgánicas
costo_fertilizacion_base_ha = 5000  # Compost sólido aplicación inicial pocetas
costo_fertirrigacion_liquida_ha = 3000  # Biofertilizantes líquidos inyectados vía Venturi
costo_energia_riego_ha = 5000  # Electricidad bomba + mantenimiento sistema goteo
costo_mano_obra_ha = 25000  # Siembra, manejo, cosecha (3 ciclos)
costo_operativo_anual_ha = 41000  # TOTAL/ha/año
```

| Parámetro | Valor Base | Componentes | Impacto |
|-----------|------------|-------------|---------|
| **`costo_semillas_ha`** | $3,000 | Maíz criollo + frijol Jamapa + calabaza orgánica | 🟢 Medio |
| **`costo_fertilizacion_base_ha`** | $5,000 | Compost orgánico sólido (aplicación inicial sustrato pocetas) | 🟡 Alto |
| **`costo_fertirrigacion_liquida_ha`** | $3,000 | **Biofertilizantes líquidos inyectados vía sistema Venturi** | 🟡 Alto |
| **`costo_energia_riego_ha`** | $5,000 | Electricidad bomba + mantenimiento sistema goteo | 🟡 Alto |
| **`costo_mano_obra_ha`** | $25,000 | Siembra, deshierbe, cosecha (3 ciclos × $8,333/ciclo) | 🔴 **CRÍTICO** |

**✅ MODELO DE FERTIRRIGACIÓN:**

El sistema utiliza **fertirrigación con fertilizantes líquidos orgánicos inyectados** al sistema de riego por goteo mediante **sistemas Venturi**:

**Componentes del costo (3 líneas separadas):**

1. **`costo_fertilizacion_base_ha = $5,000`** 
   - Compost orgánico sólido certificado
   - Aplicación inicial al sustrato en pocetas (año 1)
   - Reposición parcial anual (20-30%)
   - ~2,000 kg/ha × $2.50/kg

2. **`costo_fertirrigacion_liquida_ha = $3,000`** ✅ **PALANCA CRÍTICA**
   - Biofertilizantes líquidos orgánicos (ácidos húmicos, aminoácidos, extractos microbianos)
   - Inyección continua vía sistema Venturi en línea de riego
   - Dosis: 50-100 L/ha/año × $30-60/L
   - Aplicación: 3 ciclos × 15-20 aplicaciones/ciclo

3. **`costo_energia_riego_ha = $5,000`**
   - Electricidad bomba sumergible (pozo profundo)
   - Mantenimiento sistema goteo (filtros, válvulas, goteros)
   - ~15,000 kWh/ha/año × $0.30/kWh = $4,500 + $500 mantenimiento

**Total sistema fertirrigación = $13,000/ha/año**

**🔧 Tecnología Venturi:**
- Inyector proporcional por presión diferencial (sin energía eléctrica adicional)
- Ratio inyección: 0.5-2.0% del caudal riego
- Permite mezcla homogénea fertilizantes orgánicos líquidos
- Costo equipo: ~$8,000 (incluido en `costo_riego_ha` inversión inicial)

**⚠️ Consideración costos:** Valores actuales son **conservadores**. Validar con:
- Proveedores biofertilizantes orgánicos certificados Yucatán
- Tarifa eléctrica agrícola CFE (puede variar $0.25-0.40/kWh)
- Si costo_fertirrigacion_liquida_ha sube a $5,000 → ROI cae ~2-3%

---

### **4. PRECIOS DE VENTA** (Líneas 36-38) 🎛️ **3 PALANCAS CRÍTICAS**

```python
precio_maiz_t = 8000  # Forraje uso interno (costo oportunidad)
precio_frijol_jamapa_t = 35000  # Frijol orgánico comercial
precio_pepita_calabaza_t = 80000  # Semilla calabaza premium orgánica
```

| Parámetro | Valor Base | Rango Válido | Mercado/Destino | Impacto ROI |
|-----------|------------|--------------|-----------------|-------------|
| **`precio_maiz_t`** 🎛️ | $8,000/t | $6,000 - $10,000 | FVH interno (vs $6,500 mercado convencional) | 🟡 **±4%** (25% ingreso) |
| **`precio_frijol_jamapa_t`** 🎛️ | $35,000/t | $18,000 - $45,000 | Venta orgánica certificada (vs $18k convencional) | 🔴 **±18%** (50% ingreso) |
| **`precio_pepita_calabaza_t`** 🎛️ | $80,000/t | $45,000 - $100,000 | Export premium (vs $45k nacional) | 🟡 **±7%** (25% ingreso) |

**🎛️ PALANCAS DE PRECIOS - Análisis de Sensibilidad:**

**Escenarios de precio por producto:**

1. **Precio Frijol Jamapa** (PALANCA #1 - impacto ±18% ROI):
   - **Pesimista:** $25,000/t (-29%) → ROI año 5 cae a **~85%**
   - **Base:** $35,000/t → ROI **122.7%**
   - **Optimista:** $45,000/t (+29%) → ROI año 5 sube a **~160%**

2. **Precio Pepita Calabaza** (PALANCA #6 - impacto ±7% ROI):
   - **Pesimista:** $60,000/t (-25%) → ROI año 5 cae a **~114%**
   - **Base:** $80,000/t → ROI **122.7%**
   - **Optimista:** $100,000/t (+25%) → ROI año 5 sube a **~145%**

3. **Precio Maíz FVH** (PALANCA #7 - impacto ±4% ROI):
   - **Pesimista:** $6,500/t (-19%) → ROI año 5 cae a **~118%**
   - **Base:** $8,000/t → ROI **122.7%**
   - **Optimista:** $9,500/t (+19%) → ROI año 5 sube a **~127%**
   - **Nota:** Es costo oportunidad (ahorro en compra para FVH, no venta directa)

**Combinaciones críticas:**
- **Peor escenario (3 precios bajos):** Frijol $25k + Pepita $60k + Maíz $6.5k → ROI **~73%**
- **Mejor escenario (3 precios altos):** Frijol $45k + Pepita $100k + Maíz $9.5k → ROI **~185%**
- **Escenario conservador:** Frijol $30k + Pepita $70k + Maíz $7.5k → ROI **~105%**

---

### **5. MEJORA PRODUCTIVIDAD ANUAL** (Líneas 40-42)

```python
mejora_productividad = [1.0, 1.1, 1.1, 1.15, 1.15]
# Año 1: 100%, Año 2-3: +10%, Año 4-5: +15%
```

| Año | Factor | Justificación Agronómica |
|-----|--------|-------------------------|
| **1** | 1.0 | Sistema nuevo, sustrato inicial, plantas adaptándose |
| **2-3** | 1.1 | Mejora suelo por biofábricas, residuos cultivos anteriores |
| **4-5** | 1.15 | Estabilización microbiológica, materia orgánica acumulada |

**⚠️ Supuesto conservador:** SPCM reporta +20-25% en año 3, aquí solo +15% máximo.

**Editar para escenarios:**
- **Pesimista:** `[1.0, 1.0, 1.05, 1.05, 1.1]` (suelo degradado más lento)
- **Optimista:** `[1.0, 1.15, 1.2, 1.25, 1.25]` (manejo intensivo biofábricas)

---

### **6. ÁREA DEL PROYECTO** (Línea 54)

```python
ha_lote = 20  # Hectáreas totales del proyecto
```

| Parámetro | Valor Base | Efecto en Cálculos |
|-----------|------------|-------------------|
| **`ha_lote`** | 20 ha | 🔴 **CRÍTICO**: Multiplica todos los costos/ingresos totales |

**Cambiar para análisis de escalamiento:**
- **Piloto:** `ha_lote = 5` (1 subsección)
- **Fase 1:** `ha_lote = 20` (actual)
- **Expansión:** `ha_lote = 100` o `250` (capacidad total)

**⚠️ Punto de equilibrio actual:** 12.5 ha (calculado por el script)
- Con 20 ha → 1.6x sobre equilibrio
- Con 100 ha → 8x sobre equilibrio

---

## 📊 COSTOS DE INVERSIÓN INICIAL (NO EDITABLES - CALCULADOS)

### **Costos de Infraestructura por Hectárea** (Líneas 18-26)

```python
costo_equipo_2_retroexcavadoras = 3,160,000  # 2 CAT 420F usadas
costo_aditamento_fae = 235,000  # FAE DML/HY forestry mulcher
costo_equipo_total = 3,395,000

costo_desmonte_ha = 24,700  # Limpieza FAE (0.3 meses/5ha)
costo_excavacion_ha = 251,800  # 2 retros: 12 meses/5ha
costo_sustrato_ha = 44,000  # Compost + fibra coco
costo_riego_ha = 45,000  # Sistema goteo + fertirrigación
```

**Total infraestructura/ha = $465,500** (20 ha = $9,310,000)

Estos valores son **resultados del análisis de tiempos de excavación** (ver [`analisis_tiempos_excavacion.tex`](analisis_tiempos_excavacion.tex)). Solo editar si cambia la estrategia de equipo.

---

## 🎯 OUTPUTS PRINCIPALES DEL SCRIPT

### **1. Rendimientos por Hectárea (Año 1)**
- Maíz: 10.5 t/ha/año (3.5 t/ciclo × 3)
- Frijol: 3.9 t/ha/año (1.3 t/ciclo × 3)
- Pepita: 1.2 t/ha/año (0.4 t/ciclo × 3)

### **2. Inversión Inicial Total**
- **$13,791,750 MXN** para 20 ha
  - Equipo: $3,395,000
  - Desmonte: $494,000
  - Excavación: $5,036,000
  - Sustrato: $880,000
  - Riego: $900,000
  - Pozos: $2,000,000
  - FVH: $250,000
  - Otros: $836,750

### **3. Punto de Equilibrio**
- **12.5 hectáreas** (274,454 pocetas)
- Ahorro neto vs excavación contratada: $2,047,800

### **4. ROI Acumulado (5 años)**
- Año 1: -60.1% (inversión inicial)
- Año 3: +29.0% (breakeven)
- **Año 5: +122.7%** (retorno final)

### **5. Ingresos por Producto (Promedio Anual)**
- Maíz (forraje interno): 25.6% de ingresos
- **Frijol Jamapa (venta):** 49.8% de ingresos
- Pepita calabaza (venta): 24.6% de ingresos

---

## 🔍 ANÁLISIS DE SENSIBILIDAD

### **Variables de Mayor Impacto en ROI (Ordenadas)**

| Variable | Cambio ±10% | Efecto en ROI Año 5 | Prioridad |
|----------|-------------|---------------------|-----------|
| **`precio_frijol_jamapa_t`** | $31,500 - $38,500 | ±18% | 🔴 CRÍTICA |
| **`supervivencia`** | 0.72 - 0.88 | ±15% | 🔴 CRÍTICA |
| **`rend_frijol_por_planta_ciclo`** | ±10% | ±12% | 🔴 CRÍTICA |
| **`costo_mano_obra_ha`** | $22,500 - $27,500 | ±8% | 🟡 Alta |
| **`ciclos_por_ano`** | 2.7 - 3.3 (no usar, solo 3) | ±10% | 🟡 Alta |
| **`precio_pepita_calabaza_t`** | $72,000 - $88,000 | ±7% | 🟡 Alta |
| **`mejora_productividad[4]`** | 1.04 - 1.27 | ±5% | 🟢 Media |
| **`costo_fertilizante_organico_ha`** | $7,200 - $8,800 | ±3% | 🟢 Media |
| **`precio_maiz_t`** | $7,200 - $8,800 | ±4% | 🟢 Media |

**Recomendación:** Enfocarse en:
1. **Certificación orgánica** del frijol Jamapa (mantener precio premium $35k/t)
2. **Mejorar supervivencia** al 85% (capacitación siembra + sustrato optimizado)
3. **Contratos anticipados** pepita export ($80-100k/t garantizado)

---

## 🚨 ALERTAS Y VALIDACIONES

### **Validaciones Automáticas Recomendadas (Futuras Mejoras)**

```python
# Validar densidad pocetas
if pocetas_por_ha < 15000 or pocetas_por_ha > 30000:
    print("⚠️ ADVERTENCIA: Densidad fuera de rango SPCM (15k-30k)")

# Validar supervivencia
if supervivencia < 0.6:
    print("⚠️ ERROR: Supervivencia muy baja, revisar técnica siembra")
elif supervivencia > 0.9:
    print("⚠️ ADVERTENCIA: Supervivencia alta inusual para siembra directa")

# Validar rendimientos vs SPCM
rend_maiz_ciclo = rend_maiz_anual_base / ciclos_por_ano
if rend_maiz_ciclo > 3.5:
    print(f"⚠️ ERROR: Maíz {rend_maiz_ciclo:.1f} t/ha/ciclo excede meta SPCM (3.5 t)")

# Validar mix policultivo
if plantas_frijol_ha > plantas_maiz_ha:
    print("⚠️ ADVERTENCIA: Frijol domina sobre maíz (revisar milpa tradicional)")
```

---

## 📝 RECOMENDACIONES DE USO

### **Escenario 1: Validar Cambios en Densidad Siembra**
```python
# Probar diferentes densidades
for pocetas in [18000, 22000, 26000]:
    pocetas_por_ha = pocetas
    # Ejecutar script y comparar ROI
```

### **Escenario 2: Ajustar por Variedad de Frijol**
Si cambias de **Jamapa** a **Negro Veracruz**:
```python
rend_frijol_por_planta_ciclo = 0.000042  # +14% rendimiento
precio_frijol_jamapa_t = 28000  # -20% precio (menos premium)
# Resultado neto: Similar ingreso
```

### **Escenario 3: Sistema Sin Riego (Milpa Tradicional)**
```python
ciclos_por_ano = 1  # Solo temporada lluvias
supervivencia = 0.6  # Sin riego técnico
rend_maiz_por_planta_ciclo = 0.000050  # -24% por estrés hídrico
mejora_productividad = [1.0, 1.0, 1.0, 1.0, 1.0]  # Sin mejora continua
# ROI caería a ~35% en año 5
```

### **Escenario 4: Expansión a 100 hectáreas**
```python
ha_lote = 100
# Punto equilibrio sigue en 12.5 ha
# ROI mejora por economías de escala (menos costos equipo/ha)
```

---

## 📞 PREGUNTAS FRECUENTES

### **P1: ¿Por qué la supervivencia es 80% y no 95%?**
**R:** Siembra directa en suelo cárstico tiene mortalidad inicial por:
- Ataque de pájaros (10-15% en primeras semanas)
- Estrés hídrico inicial (5-10% antes de establecer riego)
- Plagas de suelo (5% aprox.)
- 80% es **conservador** vs 85-90% reportado en SPCM bajo manejo óptimo.

### **P2: ¿Incluye el costo de la electricidad para fertirrigación?**
**R:** **SÍ**, separado en TRES líneas:
- `costo_fertilizacion_base_ha = $5,000` → Compost sólido aplicación inicial pocetas
- `costo_fertirrigacion_liquida_ha = $3,000` → **Biofertilizantes líquidos inyectados vía Venturi**
- `costo_energia_riego_ha = $5,000` → **Electricidad bomba + mantenimiento equipo**

**Total sistema fertirrigación = $13,000/ha/año**

**✅ Modelo implementado:** Fertirrigación con fertilizantes líquidos orgánicos inyectados al sistema de riego por goteo mediante **sistemas Venturi** (inyección proporcional por presión diferencial).

### **P3: ¿Cómo ajusto si compro solo 1 retroexcavadora?**
**R:** Modificar líneas 19-22:
```python
costo_equipo_2_retroexcavadoras = 1580000  # Solo 1 CAT 420F
costo_excavacion_ha = 503580  # 24 meses/5ha (doble tiempo)
# Primer cosecha se retrasa de mes 17 a mes 46
# ROI cae porque pierdes 2 años de ingresos
```

### **P4: ¿El script considera degradación del sustrato?**
**R:** **NO**, actualmente asume sustrato permanente. 

**Mejora recomendada:** Agregar reposición año 4:
```python
# En el loop año 4
if ano == 4:
    costo_reposicion_sustrato = 22000 * ha_lote  # 50% sustrato
    costos_operativos += costo_reposicion_sustrato
```

---

## 📚 REFERENCIAS TÉCNICAS

1. **Investigación SPCM:** Larqué-Saavedra et al. (CICY) - Ver carpeta `2025. maiz continuo/`
2. **Análisis de equipo:** [`analisis_tiempos_excavacion.tex`](analisis_tiempos_excavacion.tex) (34 páginas)
3. **Proyección financiera:** [`reporte_proyeccion_5anos.tex`](reporte_proyeccion_5anos.tex) (18 páginas)
4. **Validación técnica:** [`validacion_tecnica_academica.tex`](validacion_tecnica_academica.tex) (22 páginas)

---

## 📞 SOPORTE TÉCNICO

**Para modificaciones o dudas:**
- Agronomía/Rendimientos: Revisar papers SPCM en `2025. maiz continuo/`
- Costos/Equipo: Ver memoria cálculo en `analisis_tiempos_excavacion.tex`
- Precios orgánicos: Consultar [`terra_maya_conversacion.txt`](terra_maya_conversacion.txt) (datos mercado Yucatán)

---

**Última actualización:** Diciembre 2025  
**Versión:** 1.0 (Estrategia 2 retroexcavadoras + FAE)
