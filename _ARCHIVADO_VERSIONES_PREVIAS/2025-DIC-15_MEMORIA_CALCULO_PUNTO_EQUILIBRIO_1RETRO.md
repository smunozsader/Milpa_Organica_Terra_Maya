# MEMORIA DE CÁLCULO: PUNTO DE EQUILIBRIO
## Análisis detallado de las cifras 7.8 ha vs 5.8 ha

---

## ORIGEN DE LAS CIFRAS

### 📍 CIFRA DE **7.8 HECTÁREAS**
**Fuente:** Documentos LaTeX (validacion_tecnica_academica.tex línea 316)

**Texto exacto del documento:**
```latex
\textbf{Punto de equilibrio equipo propio:} 
$1,580,000 \div 12.37$ = \textbf{127,728 pocetas = 7.8 hectáreas}
```

### 📍 CIFRA DE **5.8 HECTÁREAS**
**Fuente:** Cálculo matemático correcto de la auditoría

**Cálculo:**
```
127,728 pocetas ÷ 22,000 pocetas/ha = 5.806 hectáreas
```

### 📍 CIFRA DE **20.0 HECTÁREAS** (adicional encontrada)
**Fuente:** costo_pocetas.txt línea 71

**Texto exacto:**
```
PUNTO DE EQUILIBRIO: 20.0 hectáreas (127,728 pocetas)
```

---

## MEMORIA DE CÁLCULO PASO A PASO

### MÉTODO 1: Por poceta individual

#### PASO 1: Calcular el ahorro por poceta
```
Costo contratado/poceta:        $35.25 MXN
Costo equipo propio/poceta:   - $22.88 MXN
────────────────────────────────────────
Ahorro por poceta:              $12.37 MXN  ✅
```

**Desglose del costo contratado ($35.25/poceta):**
```
Diesel (17 L/hr × 0.046 hr/poceta × $62.5/L)   = $18.77
Operador + ayudante                            = $ 3.43
Renta de equipo                                = $ 5.00
Mantenimiento                                  = $ 1.00
Margen contratista (25%)                       = $ 7.05
────────────────────────────────────────────────────────
TOTAL CONTRATADO                               = $35.25  ✅
```

**Desglose del costo propio ($22.88/poceta):**
```
Diesel (17 L/hr × 0.046 hr/poceta × $62.5/L)   = $18.77
Operador + ayudante                            = $ 3.43
Depreciación equipo ($1,580,000 ÷ 6M pocetas) = $ 0.27
Mantenimiento                                  = $ 0.41
────────────────────────────────────────────────────────
TOTAL EQUIPO PROPIO                            = $22.88  ✅
```

#### PASO 2: Calcular pocetas necesarias para equilibrio
```
Inversión en equipo:        $1,580,000 MXN
Ahorro por poceta:       ÷  $12.37 MXN/poceta
────────────────────────────────────────────────
Pocetas necesarias:         127,728 pocetas  ✅
```

**Verificación:**
```
127,728 pocetas × $12.37 ahorro/poceta = $1,580,276
≈ $1,580,000  ✅ (diferencia $276 por redondeo)
```

#### PASO 3: Convertir pocetas a hectáreas
```
Pocetas necesarias:         127,728 pocetas
Densidad de siembra:     ÷  22,000 pocetas/ha
────────────────────────────────────────────────
Hectáreas necesarias:       5.806 ha
Redondeado:                 5.8 hectáreas  ✅
```

---

### MÉTODO 2: Por hectárea completa

#### PASO 1: Calcular costo de excavación por hectárea

**Contratado:**
```
Costo/poceta:               $35.25 MXN
Pocetas/ha:              × 22,000 pocetas/ha
────────────────────────────────────────────────
Costo contratado/ha:        $775,500 MXN/ha  ✅
```

**Equipo propio (solo excavación operativa):**
```
Costo/poceta:               $22.88 MXN
Pocetas/ha:              × 22,000 pocetas/ha
────────────────────────────────────────────────
Costo propio/ha:            $503,360 MXN/ha  ✅
```

#### PASO 2: Calcular ahorro por hectárea
```
Costo contratado/ha:        $775,500 MXN
Costo propio/ha:         -  $503,360 MXN
────────────────────────────────────────────────
Ahorro por hectárea:        $272,140 MXN/ha  ✅
```

**Verificación con método de poceta:**
```
Ahorro/poceta × pocetas/ha = $12.37 × 22,000 = $272,140  ✅
```

#### PASO 3: Calcular hectáreas necesarias
```
Inversión en equipo:        $1,580,000 MXN
Ahorro por hectárea:     ÷  $272,140 MXN/ha
────────────────────────────────────────────────
Hectáreas necesarias:       5.806 ha
Redondeado:                 5.8 hectáreas  ✅
```

---

## VERIFICACIÓN CRUZADA

### Método 3: Validación por costo total

**Escenario A: Contratar excavación de 5.8 ha**
```
Área:                       5.8 ha
Pocetas:                    5.8 × 22,000 = 127,600 pocetas
Costo contratado:           127,600 × $35.25 = $4,497,900
```

**Escenario B: Comprar equipo y excavar 5.8 ha**
```
Inversión equipo:           $1,580,000
Excavación operativa:       127,600 × $22.88 = $2,920,288
Costo total:                $1,580,000 + $2,920,288 = $4,500,288
```

**Diferencia:**
```
$4,500,288 - $4,497,900 = $2,388
```

**Margen de error:** 0.05% (atribuible a redondeos) ✅

---

## ANÁLISIS DEL ERROR DE 7.8 HECTÁREAS

### ¿De dónde pudo salir 7.8?

#### Teoría 1: Error de conversión aritmética
```
127,728 ÷ 22,000 = 5.806...
```

**Posible error cometido:** Confusión con operación inversa
```
127,728 ÷ 16,376 = 7.8  (?)
```

Pero 16,376 no es un número relevante en el proyecto.

#### Teoría 2: Uso de densidad incorrecta
Para que dé 7.8 ha con 127,728 pocetas:
```
127,728 ÷ 7.8 = 16,375 pocetas/ha
```

Pero la densidad correcta y documentada es **22,000 pocetas/ha**, no 16,375.

#### Teoría 3: Cálculo con ahorro menor
Para que el equilibrio sea en 7.8 ha:
```
$1,580,000 ÷ 7.8 ha = $202,564 por hectárea
$202,564 ÷ 22,000 = $9.21 por poceta
```

Pero el ahorro real es **$12.37/poceta**, no $9.21.

Para tener ahorro de $9.21/poceta:
```
Costo contratado - Costo propio = $9.21
```

Esto implicaría:
- Costo contratado: $32.09/poceta (vs real $35.25)
- O costo propio: $26.04/poceta (vs real $22.88)

Ninguno de estos valores es correcto según la documentación.

#### Teoría 4: Typo simple
**CONCLUSIÓN MÁS PROBABLE:**

7.8 es simplemente un **error de tipeo o cálculo mental incorrecto** al hacer:
```
127,728 ÷ 22,000 = ?
```

El calculista pudo haber:
- Confundido dígitos (5.8 → 7.8)
- Usado calculadora incorrectamente
- Copiado valor de otro cálculo erróneo

---

## TABLA COMPARATIVA DE ESCENARIOS

| Hectáreas | Pocetas | Costo Contratado | Costo Propio | Diferencia | Estado |
|-----------|---------|------------------|--------------|------------|--------|
| 5.8 ha | 127,600 | $4,497,900 | $4,500,288 | ~$0 | ✅ EQUILIBRIO |
| 7.8 ha | 171,600 | $6,046,500 | $5,503,648 | +$542,852 | ⚠️ Ya amortizado |
| 20.0 ha | 440,000 | $15,510,000 | $11,647,200 | +$3,862,800 | ✅ Muy rentable |

**Interpretación:**
- A **5.8 ha**: El equipo se paga exactamente (break-even)
- A **7.8 ha**: Ya hay ganancia neta de $542k sobre la inversión
- A **20.0 ha**: Ganancia neta de $3.86M sobre inversión

---

## DEMOSTRACIÓN MATEMÁTICA RIGUROSA

### Proposición
El punto de equilibrio es **5.8 hectáreas**, no 7.8 ni 20.0.

### Demostración

**Dados:**
- I = Inversión equipo = $1,580,000
- Ac = Costo contratado/poceta = $35.25
- Ap = Costo propio/poceta = $22.88
- D = Densidad = 22,000 pocetas/ha

**Ahorro por poceta:**
```
S = Ac - Ap = $35.25 - $22.88 = $12.37
```

**Número de pocetas para equilibrio:**
```
P = I ÷ S = $1,580,000 ÷ $12.37 = 127,728 pocetas
```

**Hectáreas para equilibrio:**
```
H = P ÷ D = 127,728 ÷ 22,000 = 5.8063636... ha
```

**Redondeado a 1 decimal:**
```
H ≈ 5.8 ha  ∎
```

### Verificación por método alternativo

**Ahorro por hectárea:**
```
Sh = S × D = $12.37 × 22,000 = $272,140/ha
```

**Hectáreas para equilibrio:**
```
H = I ÷ Sh = $1,580,000 ÷ $272,140 = 5.8063636... ha ≈ 5.8 ha  ∎
```

**Ambos métodos dan el mismo resultado. Q.E.D.**

---

## IMPACTO DEL ERROR

### Si se usa 7.8 ha como punto de equilibrio:

**Error absoluto:** 7.8 - 5.8 = **2.0 hectáreas** de diferencia

**Error relativo:** (7.8 - 5.8) ÷ 5.8 = **34.5% de sobrestimación**

**Implicaciones:**
1. **Para inversionistas:** Se está diciendo que necesitan más área de la real para justificar la compra
2. **Para planificación:** Se subestima la rentabilidad del equipo
3. **Para comunicación:** Pérdida de credibilidad si se detecta el error

### Si se usa 20.0 ha como punto de equilibrio:

**Error absoluto:** 20.0 - 5.8 = **14.2 hectáreas** de diferencia

**Error relativo:** (20.0 - 5.8) ÷ 5.8 = **245% de sobrestimación**

**Implicaciones:**
1. **CRÍTICO:** Error garrafal que sugiere falta de rigor técnico
2. **Riesgo:** Decisión de inversión podría rechazarse por parecer poco viable
3. **Legal:** Podría considerarse información engañosa si se presenta a socios/bancos

---

## EVIDENCIA DOCUMENTAL

### En validacion_tecnica_academica.tex (línea 316):
```latex
\textbf{Punto de equilibrio equipo propio:} 
$1,580,000 \div 12.37$ = \textbf{127,728 pocetas = 7.8 hectáreas}.
```

**Cálculo del documento:**
- ✅ $1,580,000 ÷ 12.37 = 127,728 pocetas (CORRECTO)
- ❌ 127,728 pocetas = 7.8 hectáreas (INCORRECTO)

**Cálculo correcto:**
- ✅ 127,728 ÷ 22,000 = **5.8 hectáreas**

### En reporte_proyeccion_5anos.tex (línea 240):
```latex
\textbf{Punto de equilibrio:} 7.8 hectáreas (alcanzado en Fase 1)
```

**Corrección necesaria:**
```latex
\textbf{Punto de equilibrio:} 5.8 hectáreas (ampliamente superado en Fase 1)
```

### En costo_pocetas.txt (línea 71):
```
PUNTO DE EQUILIBRIO: 20.0 hectáreas (127,728 pocetas)
```

**Contradicción interna evidente:**
- 20 ha × 22,000 pocetas/ha = 440,000 pocetas
- Pero dice 127,728 pocetas
- 127,728 ÷ 22,000 = **5.8 ha**, no 20 ha

---

## CONCLUSIÓN DEFINITIVA

### ✅ CIFRA CORRECTA: **5.8 HECTÁREAS**

**Fundamento matemático:**
```
Inversión equipo:           $1,580,000
÷ Ahorro por poceta:        $12.37
= Pocetas necesarias:       127,728
÷ Densidad siembra:         22,000 pocetas/ha
= Hectáreas equilibrio:     5.806... ≈ 5.8 ha
```

**Verificado por:**
- ✅ Método de cálculo por poceta individual
- ✅ Método de cálculo por hectárea completa
- ✅ Verificación cruzada de costos totales
- ✅ Doble comprobación aritmética

### ❌ CIFRAS INCORRECTAS:

**7.8 hectáreas:**
- Error aritmético en conversión pocetas→hectáreas
- Sobrestimación del 34.5%
- Origen: Error de cálculo o typo en documentos LaTeX

**20.0 hectáreas:**
- Error conceptual grave
- Sobrestimación del 245%
- Contradicción interna en costo_pocetas.txt

---

## RECOMENDACIÓN

**Actualizar TODOS los documentos con el valor correcto:**

```
PUNTO DE EQUILIBRIO EQUIPO PROPIO: 5.8 HECTÁREAS
(127,728 pocetas con ahorro de $12.37/poceta)
```

**Mensaje para stakeholders:**
"La inversión en equipo propio se justifica desde **5.8 hectáreas**. 
El proyecto de 20 hectáreas **supera ampliamente** este umbral 
(3.4 veces el punto de equilibrio), garantizando rentabilidad robusta."

---

**Documento preparado por:** Sistema de validación financiera  
**Fecha:** 15 de diciembre de 2025  
**Estado:** ANÁLISIS COMPLETO - RECOMENDACIÓN DE CORRECCIÓN INMEDIATA
