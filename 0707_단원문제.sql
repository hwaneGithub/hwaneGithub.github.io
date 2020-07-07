-- Q1. 이름이 S로 끝나는 사원 데이터 출력
SELECT *
FROM EMP
WHERE ENAME LIKE '%S';

-- Q2. 30번 부서에서 근무하는 사원 중 직책이 SALESMAN인 사원의
-- 사원 번호, 이름, 직책, 급여, 부서 번호를 출력
SELECT EMPNO, ENAME, JOB, SAL, DEPTNO
FROM EMP
WHERE JOB = 'SALESMAN';

-- Q3. 20, 30번 부서 근무자 중 급여가 2000 초과인 사원을
-- 두 가지 방식의 SELECT문을 사용해 사원 번호, 이름, 급여, 부서 번호 출력
-- 집합 연산자 사용 안함
SELECT EMPNO, ENAME, SAL, DEPTNO
FROM EMP
WHERE DEPTNO BETWEEN 20 AND 30
  AND SAL > 2000;
  
-- 집합 연산자 사용
SELECT EMPNO, ENAME, SAL, DEPTNO
FROM EMP
WHERE DEPTNO = 20
  AND SAL > 2000
UNION
SELECT EMPNO, ENAME, SAL, DEPTNO
FROM EMP
WHERE DEPTNO = 30
  AND SAL > 2000;
  
-- Q4. NOT BETWEEN A AND B를 쓰지 않고
-- 급여가 2000 이상 3000 이하 범위 이외의 값인 데이터 출력
SELECT *
FROM EMP
WHERE SAL < 2000
  OR SAL > 3000;

-- Q5. 사원 이름에 E가 포함되어 있는 30번 부서의 사원 중
-- 급여가 1000~2000이 아닌 사원의 이름, 사원 번호, 급여, 부서 번호 출력
SELECT ENAME, EMPNO, SAL, DEPTNO
FROM EMP
WHERE SAL NOT BETWEEN 1000 AND 2000;

-- Q6. 추가 수당이 존재하지 않고 상급자가 있고 직책이 MANAGER, CLERK인 사원 중
-- 사원 이름의 두 번째 글자가 L이 아닌 사원 정보 출력
SELECT *
FROM EMP
WHERE COMM IS NULL
  AND MGR IS NOT NULL
  AND ENAME NOT LIKE '%L%'
  AND JOB = 'MANAGER'
   OR JOB = 'CLERK';
   
   
   